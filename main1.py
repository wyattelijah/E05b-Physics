import sys, logging, random, open_color, arcade

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MARGIN = 10
NUM_BALLS = 20
SCREEN_TITLE = "Gravity Exercise"

GRAVITY = -9.8 #update this value


class Ball():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.radius = 10
        self.color = color
        self.dx = 0
        self.dy = 0

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.x <= MARGIN:
            self.x = MARGIN
        if self.x >= SCREEN_WIDTH - MARGIN:
            self.x = SCREEN_WIDTH - MARGIN
        if self.y <= MARGIN:
            self.y = MARGIN
        if self.y >= SCREEN_HEIGHT - MARGIN:
            self.y = SCREEN_HEIGHT - MARGIN
    
    def accelerate(self,dx,dy):
        self.dx += dx
        self.dy += dy
    

class Window(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(True)
        arcade.set_background_color(open_color.black)
        self.ball_list = []

    def setup(self):
        for i in range(NUM_BALLS):
            x = random.randint(MARGIN,SCREEN_WIDTH-MARGIN)
            y = random.randint(MARGIN,SCREEN_HEIGHT-MARGIN)
            color = random.choice(open_color.yellows)
            self.ball = Ball(x,y,color)
            self.ball_list.append(self.ball)

    def update(self, delta_time):
        for b in self.ball_list:
            b.accelerate(0, GRAVITY)
            b.update()

    def on_draw(self):
        arcade.start_render()
        for b in self.ball_list:
            b.draw()





def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()