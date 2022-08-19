from wfc.types_ import Cell, Tile

unicode_tiles: Cell.SuperPosition = (
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

circuit_tiles: Cell.SuperPosition = (
    Tile("img/tiles/circuit_0_0.png", (Tile.Socket(0), Tile.Socket(0), Tile.Socket(1), Tile.Socket(0))),
    Tile("img/tiles/circuit_0_32.png", (Tile.Socket(0), Tile.Socket(1), Tile.Socket(1), Tile.Socket(0))),
    Tile("img/tiles/circuit_0_64.png", (Tile.Socket(0), Tile.Socket(1), Tile.Socket(0), Tile.Socket(1))),
    Tile("img/tiles/circuit_0_96.png", (Tile.Socket(0), Tile.Socket(0), Tile.Socket(1), Tile.Socket(1))),
    Tile("img/tiles/circuit_32_0.png", (Tile.Socket(1), Tile.Socket(0), Tile.Socket(1), Tile.Socket(0))),
    Tile("img/tiles/circuit_32_32.png", (Tile.Socket(1), Tile.Socket(1), Tile.Socket(1), Tile.Socket(0))),
    Tile("img/tiles/circuit_32_64.png", (Tile.Socket(1), Tile.Socket(1), Tile.Socket(1), Tile.Socket(1))),
    Tile("img/tiles/circuit_32_96.png", (Tile.Socket(1), Tile.Socket(0), Tile.Socket(1), Tile.Socket(1))),
    Tile("img/tiles/circuit_64_0.png", (Tile.Socket(1), Tile.Socket(0), Tile.Socket(0), Tile.Socket(0))),
    Tile("img/tiles/circuit_64_32.png", (Tile.Socket(1), Tile.Socket(1), Tile.Socket(0), Tile.Socket(0))),
    Tile("img/tiles/circuit_64_64.png", (Tile.Socket(1), Tile.Socket(1), Tile.Socket(0), Tile.Socket(1))),
    Tile("img/tiles/circuit_64_96.png", (Tile.Socket(1), Tile.Socket(0), Tile.Socket(0), Tile.Socket(1))),
    Tile("img/tiles/circuit_96_0.png", (Tile.Socket(0), Tile.Socket(0), Tile.Socket(0), Tile.Socket(0))),
    Tile("img/tiles/circuit_96_32.png", (Tile.Socket(0), Tile.Socket(1), Tile.Socket(0), Tile.Socket(0))),
    Tile("img/tiles/circuit_96_64.png", (Tile.Socket(0), Tile.Socket(1), Tile.Socket(0), Tile.Socket(1))),
    Tile("img/tiles/circuit_96_96.png", (Tile.Socket(0), Tile.Socket(0), Tile.Socket(0), Tile.Socket(1))),
)
