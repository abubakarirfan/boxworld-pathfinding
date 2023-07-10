
from graphics import egi
from vector2d import Vector2D


class Agent:
    def __init__(self, world, box_idx, speed):
        self.world = world
        self.box_idx = box_idx
        self.pos = world.boxes[box_idx]._vc
        self.speed = speed
        self.path = None

    def set_path(self, path):
        if self.path is None:
            self.path = path

    def update(self, delta):
        if not self.path or not self.path.path:
            return

        target_box = self.world.boxes[self.path.path[0]]
        target_pos = target_box._vc

        target_vector = Vector2D(target_pos.x, target_pos.y)
        pos_vector = Vector2D(self.pos.x, self.pos.y)

        direction = (target_vector - pos_vector).normalise()
        distance = self.speed * delta
        travel = direction * distance

        if (pos_vector + travel - target_vector).length() < distance:
            self.pos = target_pos
            self.path.path.pop(0)
            if self.path.path:
                self.box_idx = self.path.path[0]
            else:
                self.box_idx = None
        else:
            self.pos = Vector2D(pos_vector.x + travel.x, pos_vector.y + travel.y)

    def draw(self):
        egi.set_pen_color(name="BLUE")
        egi.circle(self.pos, 10)


