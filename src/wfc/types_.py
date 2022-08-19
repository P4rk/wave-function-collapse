import copy
import os.path
import random
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any

from PIL import Image


class TileRenderer:
    @staticmethod
    def is_rendereable(tile):
        return os.path.isfile(tile.tile)

    @staticmethod
    def render(tile):
        img = Image.open(tile.tile)
        return img.convert("RGB")


class CellRenderer:
    @staticmethod
    def is_renderable(cell):
        return any(TileRenderer.is_rendereable(tile) for tile in cell.super_position)

    @staticmethod
    def render(cell, height, width, dimensions, image=None):
        if cell.collapsed:
            # render tile
            if CellRenderer.is_renderable(cell):
                tile_image = TileRenderer.render(cell.super_position[0])
                image.paste(tile_image, (width*32, height*32))
                return image
            else:
                # If we are rendering the last cell we should render it with a line return
                end = ""
                if width == dimensions - 1:
                    end = "\n"
                print(cell.super_position[0].tile, end=end)
        else:
            # render possibilities
            if CellRenderer.is_renderable(cell):
                tile_image = TileRenderer.render(cell.super_position[0])
                for tile in cell.super_position[1:]:
                    tile_image = Image.blend(tile_image, TileRenderer.render(tile), 0.1)

                image.paste(tile_image, (width*32, height*32))
                return image
            else:
                # If we are rendering the last cell we should render it with a line return
                end = ""
                if width == dimensions - 1:
                    end = "\n"
                print(" ", end=end)


@dataclass(frozen=True)
class Tile:
    """
    A possible cell option
    """
    @dataclass
    class Socket:
        """
        Given a tile, define what other tiles it can connect to using a Socket.
        A Socket can connect to another socket if they are equal.
        """
        socket: Any

    # A representation of the tile
    tile: str
    # A tuple of sockets, read in order, clockwise.
    # e.g. [0, 1, 2, 3] => [North, East, South ,West]
    sockets: tuple[Socket, ...]


@dataclass(unsafe_hash=True)
class Cell:
    """
    A position within the grid.
    Can be in a superposition e.g. has the possibility of being multiple Tiles.
    If the superposition is a single tile the Cells' superposition has collapsed, and has been fully observed.
    """

    SuperPosition = tuple[Tile, ...]

    super_position: SuperPosition
    collapsed: bool = field(default=False)

    def entropy(self) -> int:
        """
        Entropy defined by how much the superposition has collapsed.
        The smaller the superposition the more certain we are about it's content.
        """
        return len(self.super_position)

    def observe(self) -> None:
        """
        Observe a cell and collapse the superposition into a single tile.
        """
        self.collapsed = True
        random_tile_index = random.randrange(0, self.entropy())
        self.super_position = tuple([self.super_position[random_tile_index]])

    def render(self, height, width, dimensions):
        if self.collapsed:
            self.super_position[0].render(height, width, dimensions)
        if not any((tile.is_renderable() for tile in self.super_position)):
            print("")


@dataclass
class Grid:
    """
    A grid to run the WFC on.
    """
    dimensions: int
    default_super_position: tuple[Tile, ...]

    # Cells that make up the grid
    cells: list[list[Cell]] = field(init=False)
    # Whether the entire wave has collapsed
    collapsed: bool = field(init=False, default=False)

    def __post_init__(self):
        self.cells = [None] * self.dimensions
        for height in range(self.dimensions):
            self.cells[height] = [None] * self.dimensions
            for width in range(self.dimensions):
                self.cells[height][width] = Cell(copy.deepcopy(self.default_super_position))

    def __iter__(self) -> list[Cell]:
        for row in reversed(self.cells):
            yield row

    def observe(self) -> 'Grid':
        """
        Find the cell with the lowest entropy (that hasn't collapsed), and collapse it.
        """
        cells = defaultdict(list)
        for height, row in enumerate(self.cells):
            for width, cell in enumerate(row):
                if not cell.collapsed:
                    cells[cell.entropy()].append(((height, width), cell))

        if not cells:
            self.collapsed = True
            return self

        lowest_cell_entropy = min(cells.keys())
        random_cell_index = random.randrange(0, len(cells[lowest_cell_entropy]))
        (height, width), cell = cells[lowest_cell_entropy][random_cell_index]
        cell.observe()

        self._propogate_observation(height, width, cell)
        return copy.deepcopy(self)

    def _propogate_observation(self, height, width, cell) -> None:
        """
        Given an updated cell, propagate the collapse of the wave to its neighbours.
        Limit the superpositions of the neighbours based on the updated cell
        :param height: the height index of the updated cell
        :param width: the width index of the updated cell
        :param cell: the updated cell
        """
        UP = 0
        RIGHT = 1
        DOWN = 2
        LEFT = 3

        # Propagate observation to surrounding cells
        super_positions = cell.super_position

        for d_height, d_width, propagated_socket in [(-1, 0, UP), (0, -1, RIGHT), (1, 0, DOWN), (0, 1, LEFT)]:
            # Get possible sockets from the updated cell
            inverted_socket = (propagated_socket + 2) % 4
            possible_sockets = {tile.sockets[inverted_socket].socket for tile in super_positions}

            # Get the propagated cell (the cell to update)
            propagated_height = height + d_height
            propagated_width = width + d_width
            try:
                propagated_cell = self.cells[propagated_height][propagated_width]
                if propagated_cell.collapsed:
                    continue
            except IndexError:
                continue

            # Collapse the superposition of the neighbouring cell
            propagated_super_positions = propagated_cell.super_position
            new_super_position = tuple([
                propagated_tile
                for propagated_tile in propagated_super_positions
                if propagated_tile.sockets[propagated_socket].socket in possible_sockets
            ])
            propagated_cell.super_position = new_super_position

            # If we've changed the neighbour propagate it to its neighbours.
            # N.B. This has no effect for tiles with just two types of sockets.
            if len(new_super_position) != len(propagated_super_positions):
                self._propogate_observation(propagated_height, propagated_width, propagated_cell)

    def render(self) -> None:
        """
        Render the current state to the console
        """
        image = Image.new("RGB", (self.dimensions*32, self.dimensions*32))
        for height, row in enumerate(self):
            for width, cell in enumerate(row):
                image = CellRenderer.render(cell, height, width, self.dimensions, image)

        return image
