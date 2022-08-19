import time
from wfc.types_ import Grid
from wfc.tiles import unicode_tiles, circuit_tiles

#https://www.compart.com/en/unicode/block/U+2500

grid = Grid(dimensions=10, default_super_position=unicode_tiles)
stages = []
while not grid.collapsed:
    stages.append(grid.observe())

for grid_ in stages:
    time.sleep(0.1)
    print("---")
    grid_.render()
