class Agent:
  simple_reactive_agent = True

  pos_x = 1
  pos_y = 1
  vel_x = 1
  vel_y = 1

  dirt_positions = []
  dirt_count = 0

  SRA_path = [[1, 1], [1, 2], [1, 3], [1, 4],
              [2, 4], [2, 3], [2, 2], [3, 2],
              [3, 3], [3, 4], [4, 4], [4, 3],
              [4, 2], [4, 1], [3, 1], [2, 1]]
  path_index = 0

  def __init__(self, dirt_positions, dirt_count):
    self.dirt_positions = dirt_positions
    self.dirt_count = dirt_count

  def draw(self, ax):
    ax.plot([self.pos_x],[self.pos_y], marker='o', color='r', ls='')

  def update(self):
    if (self.simple_reactive_agent):
      self.pos_x = self.SRA_path[self.path_index][0]
      self.pos_y = self.SRA_path[self.path_index][1]
      self.path_index += 1
      
      if (self.path_index >= len(self.SRA_path)):
        self.path_index = 0
    else:
      pass
      # self.pos_y += self.vel_y
      # if (self.pos_y >= 5 and self.pos_x < 5):
      #   self.pos_x += self.vel_x
      #   self.pos_y -= 1
      #   self.vel_y *= -1

      # if (self.pos_y <= 1 and self.pos_x < 5):
      #   self.pos_x += self.vel_x
      #   self.pos_y += 1
      #   self.vel_y *= -1

      # if (self.pos_x >= 5 and self.pos_y < 5):
      #   self.pos_y += self.vel_y
      #   self.pos_x -= 1
      #   self.vel_x *= -1

      # if (self.pos_x <= 1 and self.pos_y < 5):
      #   self.pos_y += self.vel_y
      #   self.pos_x += 1
      #   self.vel_x *= -1

  def clean(self):
    self.dirt_count -= 1
