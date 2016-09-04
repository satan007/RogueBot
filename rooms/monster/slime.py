from constants import *
import random

name = 'Слизень'

hp = 30
element = WATER
damage_range =  ( 0, 3 )

coins = 3

loot = [ 'slime' ]

def enter(user, reply):
	msg = (
		'Это слизень. Самый обычный слизень.'
	)
	reply(msg, photo=SLIME_STICKER)

def get_actions(user):
	return user.get_fight_actions() + [ 'Раздавить' ]

def action(user, reply, text):
	if text == 'Раздавить':
		if random.random() < 0.1:
			reply('Вы не смогли раздавить слизня. Слизь поглотила вас.')
			user.death(reply)
		else:
			reply('Ты раздавил его, но запачкал обувь')
			user.add_tag('dirt')
			user.won(reply)
	else:
		user.fight_action(reply, text)