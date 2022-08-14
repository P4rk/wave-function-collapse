from wfc.types import Cell, Tile, Grid

#https://www.compart.com/en/unicode/block/U+2500
default_super_position: Cell.SuperPosition = (
    Tile(" ", (Tile.Socket(0), Tile.Socket(0), Tile.Socket(0), Tile.Socket(0))),
    Tile("═", (Tile.Socket(0), Tile.Socket(1), Tile.Socket(0), Tile.Socket(1))),
    Tile("║", (Tile.Socket(1), Tile.Socket(0), Tile.Socket(1), Tile.Socket(0))),
    Tile("╔", (Tile.Socket(0), Tile.Socket(1), Tile.Socket(1), Tile.Socket(0))),
    Tile("╚", (Tile.Socket(1), Tile.Socket(1), Tile.Socket(0), Tile.Socket(0))),
    Tile("╗", (Tile.Socket(0), Tile.Socket(0), Tile.Socket(1), Tile.Socket(1))),
    Tile("╝", (Tile.Socket(1), Tile.Socket(0), Tile.Socket(0), Tile.Socket(1))),
    Tile("╠", (Tile.Socket(1), Tile.Socket(1), Tile.Socket(1), Tile.Socket(0))),
    Tile("╣", (Tile.Socket(1), Tile.Socket(0), Tile.Socket(1), Tile.Socket(1))),
    Tile("╦", (Tile.Socket(0), Tile.Socket(1), Tile.Socket(1), Tile.Socket(1))),
    Tile("╩", (Tile.Socket(1), Tile.Socket(1), Tile.Socket(0), Tile.Socket(1))),
    Tile("╬", (Tile.Socket(1), Tile.Socket(1), Tile.Socket(1), Tile.Socket(1))),
)

grid = Grid(dimensions=10, default_super_position=default_super_position)
grid.render()
while not grid.collapsed:
    grid.observe()
    print("---")
    grid.render()
