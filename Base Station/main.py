import arcade
import os
import math

from DolphinSwarm import *
'''
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

arcade.open_window(625, 625, "Drawing Primitives Example")



arcade.set_background_color(arcade.color.GREEN)
arcade.start_render()

point_list = createPoints2Poly(6, [100, 100], 50)
arcade.draw_polygon_filled(point_list, arcade.color.WHITE)


arcade.finish_render()

arcade.run()
'''

SCREEN_WIDTH = 625
SCREEN_HEIGHT = 625
SCREEN_TITLE = "Base Station"

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.city = getCity()
        self.DSO = DSO(30, nBases[CASE]*2, (0, 625))
        pass
        

    def setup(self):
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """
        for i in self.city:
            arcade.draw_polygon_filled(i, arcade.color.WHITE)
        minumum = self.DSO.optimaze(1)
        for i in getCircles(minumum):
            arcade.draw_polygon_filled(i, (255, 0, 0, 30))



    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass


    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main method """
    #game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    #game.setup()
    #arcade.run()
    m = DSO(30, nBases[CASE], (0, 625))
    m.optimaze()


if __name__ == "__main__":
    main()