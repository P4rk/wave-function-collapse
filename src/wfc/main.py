from wfc.types_ import Grid
from wfc.tiles import (
    unicode_tiles,
    circuit_tiles,
    molecule_tiles,
    brickwall_tiles,
    border_tiles,
    celtic_tiles,
)


grid = Grid(dimensions=10, default_super_position=circuit_tiles)
stages = []
print("Collapsing...")
while not grid.collapsed:
    stages.append(grid.observe())


print("Rendering...")
images = [grid_.render() for grid_ in stages]

if any(images):
    images[0].save(
        'wfc.gif',
        save_all=True,
        append_images=images[1:],
        duration=200,
        loop=0,
    )
