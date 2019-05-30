import arcade
import math

WIDTH = 650
HEIGHT = 800

my_button = [280, 75, 50, 25]
CENTER_X = 325
CENTER_Y = 175
RADIANS_PER_FRAME1 = 0.02
SWEEP_LENGTH = 100
RADIANS_PER_FRAME2 = 0.02
RADIANS_PER_FRAME3 = 0.02


def virus_shape():
    arcade.draw_line(200, 750, 210, 725, arcade.color.WARM_BLACK, 3)
    arcade.draw_line(200, 750, 180, 780, arcade.color.WARM_BLACK, 3)
    arcade.draw_line(200, 750, 170, 740, arcade.color.WARM_BLACK, 3)
    arcade.draw_line(200, 750, 240, 730, arcade.color.WARM_BLACK, 3)
    arcade.draw_line(200, 750, 230, 770, arcade.color.WARM_BLACK, 3)

    arcade.draw_circle_filled(210, 725, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(179, 780, 6.5, arcade.color.BLACK)
    arcade.draw_circle_filled(170, 740, 6.5, arcade.color.BLACK)
    arcade.draw_circle_filled(240, 730, 7, arcade.color.BLACK)
    arcade.draw_circle_filled(230, 770, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(200, 750, 15, arcade.color.BLACK)


def types_of_malware():
    # List
    arcade.draw_text("Here are some most common types of malware:", 20, 645, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("1. Adware", 40, 630, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("2. Virus", 40, 520, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("3. Keyloggers", 40, 390, arcade.color.SMOKY_BLACK, 12)
    # Definition adware
    arcade.draw_text("Adware is the least dangerous and most lucrative Malware.",
                     180, 590, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("It displays ads on your computer.", 180, 575, arcade.color.SMOKY_BLACK, 12)
    # Definition virus
    arcade.draw_text("A virus is a contagious program or code that attaches itself to",
                     180, 485, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("another piece of software, and then reproduces itself when",
                     180, 470, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("that software is run. Most often this is spread by sharing",
                     180, 455, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("software or files between computers.", 180, 440, arcade.color.SMOKY_BLACK, 12)
    # Definition Kevloggers
    arcade.draw_text("A kevloggers records everything you type on your PC in order to",
                     180, 365, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("glean your log-in names, passwords, and other sensitive",
                     180, 350, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("information, and send it on to the source of the keylogging",
                     180, 335, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("program. Many times keyloggers are used by corporations and",
                     180, 320, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("parents to acquire computer usage information.", 180, 305, arcade.color.SMOKY_BLACK, 12)


def definition_of_what_is_malware():
    arcade.draw_text("Malware, or malicious software, is any program or file that is harmful to a computer user.",
                     20, 705, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("Types of malware can include computer viruses, worms, Trojan horses and spyware.",
                     20, 690, arcade.color.SMOKY_BLACK, 12)


def how_to_avoid_malware():
    arcade.draw_text("After knowing types of malwares, and the way malwares harms the computer,",
                     50, 230, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("the question of \"How do we prevent the hidden danger with malwares?\"",
                     50, 215, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("We can prevent the hidden danger with these actions:", 50, 190, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("Install ad-blocker", 50, 175, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("Install(have) anti-virus software", 50, 160, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("Secure the network(Use WPA or WPA2 encryption)", 50, 145, arcade.color.SMOKY_BLACK, 12)
    arcade.draw_text("Prevent accessing inappropriate websites and \'buttons\'", 50, 130, arcade.color.SMOKY_BLACK, 12)


def square_point(x, y):
    arcade.draw_point(x, y, arcade.color.BLUE, 5)


def on_update(delta_time):
    pass


def on_draw():
    arcade.start_render()
    global x1, y1
    # Draw in here...
    # Antivirus Software
    on_draw.angle1 += RADIANS_PER_FRAME1
    on_draw.angle2 += RADIANS_PER_FRAME2
    on_draw.angle3 += RADIANS_PER_FRAME3

    x = SWEEP_LENGTH * math.sin(on_draw.angle1) + CENTER_X
    y = SWEEP_LENGTH * math.cos(on_draw.angle1) + CENTER_Y
    a = SWEEP_LENGTH * math.sin(on_draw.angle2) + CENTER_X
    b = SWEEP_LENGTH * math.cos(on_draw.angle2) + CENTER_Y
    e = SWEEP_LENGTH * math.sin(on_draw.angle3) + CENTER_X
    f = SWEEP_LENGTH * math.cos(on_draw.angle3) + CENTER_Y

    arcade.start_render()

    texture_10 = arcade.load_texture("1.png")
    scale_10 = 0.15
    arcade.draw_texture_rectangle(x, y, scale_10 * texture_10.width, scale_10 * texture_10.height, texture_10, 0)

    texture_11 = arcade.load_texture("2.png")
    scale_11 = 0.15
    arcade.draw_texture_rectangle(a, b, scale_11 * texture_11.width, scale_11 * texture_11.height, texture_11, 0)
    texture_12 = arcade.load_texture("3.png")
    scale_12 = 0.375
    arcade.draw_texture_rectangle(e, f, scale_12 * texture_12.width, scale_12 * texture_12.height, texture_12, 0)
    # Virus Shape
    virus_shape()
    # Mouse on click text
    arcade.draw_text("Click This!", 350, 80, arcade.color.SMOKY_BLACK, 15)
    arcade.draw_xywh_rectangle_filled(my_button[0],
                                      my_button[1],
                                      my_button[2],
                                      my_button[3],
                                      arcade.color.LIGHT_CORNFLOWER_BLUE)
    # Title
    arcade.draw_text("__________________", 247, 750, arcade.color.BLACK, 15)
    arcade.draw_text("Malware Prevention", 250, 750, arcade.color.BLACK, 15)
    # What is malware
    square_point(10, 725)
    arcade.draw_text("What is Malware", 20, 720, arcade.color.BLACK, 13)
    # Definition of what is malware
    definition_of_what_is_malware()
    # Types of malware
    square_point(10, 665)
    arcade.draw_text("Types of Malware", 20, 660, arcade.color.BLACK, 13)
    # Lists of malwars
    types_of_malware()
    # Pictures
    texture_1 = arcade.load_texture("adware_graphics_1.jpg")
    scale_1 = 0.2
    arcade.draw_texture_rectangle(90, 580, scale_1 * texture_1.width, scale_1 * texture_1.height, texture_1, 0)

    texture_2 = arcade.load_texture("Virus.png")
    scale_2 = 0.12
    arcade.draw_texture_rectangle(90, 460, scale_2 * texture_2.width, scale_2 * texture_2.height, texture_2, 0)

    texture_3 = arcade.load_texture("keylogger.png")
    scale_3 = 0.25
    arcade.draw_texture_rectangle(90, 330, scale_3 * texture_3.width, scale_3 * texture_3.height, texture_3, 0)
    # How to prevent malware
    how_to_avoid_malware()
    square_point(40, 180)
    square_point(40, 165)
    square_point(40, 150)
    square_point(40, 135)


on_draw.angle1 = 0
on_draw.angle2 = 120
on_draw.angle3 = 240


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    my_button_x, my_button_y, my_button_w, my_button_h = my_button

    # Need to check all four limits of the button.
    if (x > my_button_x and x < my_button_x + my_button_w and y > my_button_y and y < my_button_y + my_button_h):
        print("You Clicked The Button!!! This could've get you Malware Virus!!!")
    else:
        print("Good job, you did not click this dangerous button")


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Poster - Malware Prevention")
    arcade.set_background_color(arcade.color.LIGHT_GRAY)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_update = on_update
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
