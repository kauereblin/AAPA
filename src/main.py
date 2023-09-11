import numpy as np
import matplotlib.pyplot as plt
import random
from Agent import Agent

DIRT_COUNT = 6

# board = np.zeros((6, 6))
# wall_locations = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), # top
#                   (1, 5), (2, 5), (3, 5), (4, 5), (5, 5),         # right
#                   (5, 0), (5, 1), (5, 2), (5, 3), (5, 4),         # left
#                   (1, 0), (2, 0), (3, 0), (4, 0)]                 # botton

# BOARD
fig, ax = plt.subplots()
fig.suptitle("Agente Aspirador de Pó Automático (AAPA)")
fig.set_size_inches(10, 10)

# GRID
ax.set_xticks(np.arange(-0.5, 6.5, 1))
ax.set_yticks(np.arange(-0.5, 6.5, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(color='black', linewidth=3)

def get_random_coordinates():
    x_range = range(1, 5)
    y_range = range(1, 5)

    return random.sample([(x, y) for x in x_range for y in y_range], DIRT_COUNT);

def draw_flor():
    rows = []
    cols = []
    for row in range(1, 5):
        for col in range(1, 5):
            rows.append(row)
            cols.append(col)
    ax.plot(rows, cols, markersize=91, marker='s', color='b', ls='');

def draw_walls():
    ax.plot([0, 0, 0, 0, 0, 0,
            1, 2, 3, 4, 5,
            5, 5, 5, 5, 5,
            4, 3, 2, 1],
            [0, 1, 2, 3, 4, 5,
            5, 5, 5, 5, 5,
            4, 3, 2, 1, 0,
            0, 0, 0, 0], markersize=91, marker='s', color='g', ls='')

dirt_positions = get_random_coordinates()
def draw_dirt():
    for pos in dirt_positions:
        ax.plot(pos[0], pos[1], markersize=91, marker='s', color='y', ls='')

agent_sra = Agent(dirt_positions, DIRT_COUNT)

while True:
    draw_walls()
    draw_flor()
    draw_dirt()
    agent_sra.draw(ax)
    plt.show(block=False)
    plt.pause(0.5)

    agent_sra.update()

    for dirt_position in dirt_positions:
        if (agent_sra.pos_x == dirt_position[0] and agent_sra.pos_y == dirt_position[1]):
            dirt_positions.remove(dirt_position)
            break




















# if __name__ == "__main__":
#     pass