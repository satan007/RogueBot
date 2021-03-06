import rooms.roomloader as roomloader

name = 'Распутье'

room_type = 'other'

def get_actions(user):
	rooms = user.get_room_temp('rooms')

	actions = [ ]

	for room_type, room_name in rooms:
		loaded_room = roomloader.load_room(room_name, room_type)
		actions.append(loaded_room.name)

	return actions

def enter(user, reply):
	rooms = [ roomloader.get_next_room() for i in range(3) ]
	user.set_room_temp('rooms', rooms)

def action(user, reply, text):
	rooms = user.get_room_temp('rooms')
	for room_type, room_name in rooms:
		loaded_room = roomloader.load_room(room_name, room_type)
		if loaded_room.name == text:
			user.open_room(reply, room_type, room_name)
			return

	reply('Такого выбора тебе не давали')

