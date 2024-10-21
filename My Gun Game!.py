from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

class Ground(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            texture='brick',
            collider='box',
            color=color.gray,
            scale=(1000, 1, 1000)
        )
        

gun = Entity(model='cube', color=color.gray, scale=(0.2, 0.1, 0.5), position=(0.2, -0.2, 0.6), parent=camera.ui)
bullets = []

def shoot():
    bullet = Entity(model='sphere', color=color.yellow, scale=0.2,
                    position=player.position + (player.forward * 2),
                    collider='box')
    bullet.animate_position(bullet.position + (player.forward * 20), duration=1, curve=curve.linear)
    bullets.append(bullet)
    destroy(bullet, delay=1.5)

def update():
    if held_keys['left mouse']:
        shoot()


Sky(color=color.gray)
player = FirstPersonController()
window.fullscreen = True

Ground()

app.run()
