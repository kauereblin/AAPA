class Agent:
  score = 0
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

  def calculate_distance(self, coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

  def sort_coordinates(self, coords):
      sorted_coords = []
      current_coord = coords[0]
      
      lista = []
      for _ in coords:
          lista.append(_)

      lista.remove(current_coord)
    
      while lista:
          nearest_coord = min(lista, key=lambda x: self.calculate_distance(current_coord, x))
          sorted_coords.append(nearest_coord)
          lista.remove(nearest_coord)
          current_coord = nearest_coord
      
      sorted_coords.insert(0, coords[0])

      return sorted_coords

  def __init__(self, dirt_positions, dirt_count, sra):
    self.pos_x = 1
    self.pos_y = 1
    self.dirt_count = dirt_count
    self.simple_reactive_agent = sra

    # SORT DIRT POSITIONS
    self.dirt_positions.sort()
    self.dirt_positions = self.sort_coordinates(dirt_positions)

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
      if (len(self.dirt_positions) > 0):
        dirt_x = self.dirt_positions[0][0]
        dirt_y = self.dirt_positions[0][1]

      if (self.dirt_count == len(self.dirt_positions) and self.dirt_count > 0):
        distance_x = dirt_x - self.pos_x
        distance_y = dirt_y - self.pos_y
        
        if (self.pos_x == dirt_x and self.pos_y == dirt_y):
          self.pos_x += self.vel_x
          self.score += 1
        elif (abs(distance_x) > abs(distance_y)):
          self.pos_x += self.vel_x * (1 if distance_x > 0 else - 1)
          self.score += 1
        elif (abs(distance_y) > abs(distance_x)):
          self.pos_y += self.vel_y * (1 if distance_y > 0 else - 1)
          self.score += 1
        else:
          self.pos_x += self.vel_x * (1 if distance_x > 0 else - 1)
          self.score += 1

  def clean(self):
    self.score += 1
    self.dirt_positions.remove([self.pos_x, self.pos_y])
    self.dirt_count -= 1
