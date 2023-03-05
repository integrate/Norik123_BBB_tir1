import time,wrap, random, math
from time import sleep
from wrap import sprite, actions, world, sprite_text
from random import randint, choice

world.create_world(600, 600, 680, 30)

hero = sprite.add("battle_city_tanks", 100, 100, "tank_player_size1_green1")

spisok_bullet=[]
spisok_star=[]

@wrap.always(1000)
def show_star():
    y = randint(1, 500)
    x = randint(1, 600)
    star = sprite.add("battle_city_items", x, y, costume="block_gift_star")
    spisok_star.append(star)
    collide()

@wrap.on_mouse_move
def movemario(pos_x):
    sprite.move_to(hero,pos_x,550)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def shot():
    x=sprite.get_x(hero)
    y=sprite.get_top(hero)
    bullet = sprite.add("battle_city_items", x, y, costume="bullet")
    spisok_bullet.append(bullet)
    collide()

@wrap.always(50)
def bullet_move():
    for x in spisok_bullet:
        sprite.move_at_angle_dir(x,10)
        if sprite.get_y(x)<=0:
            sprite.remove(x)
            spisok_bullet.remove(x)
    collide()


def collide():
    for star in spisok_star:
        if sprite.is_collide_any_sprite(star,spisok_bullet):
            a=sprite.is_collide_any_sprite(star, spisok_bullet)
            spisok_star.remove(star)
            spisok_bullet.remove(a)
            sprite.remove(star)
            sprite.remove(a)



