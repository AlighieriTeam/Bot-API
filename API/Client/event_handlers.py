import sys


def register_events(socketio):
    @socketio.on("bot_error")
    def bot_error(data):
        print(str(data))
        sys.exit(1)
    @socketio.on("bot_connected")
    def bot_connected():
        print("Authorized")
        pass

    @socketio.on("bot_kick")
    def bot_kicked(data):
        print(data)
        sys.exit()

    @socketio.on("bot_confirm")
    def bot_confirm():
        return True

    @socketio.on("bot_start")
    def game_start(data):
        print(data)

    @socketio.on("bot_ask")
    def bot_ask(data):
        print(data)
        import random
        act = random.randint(0, len(data) - 1)
        print(f"Chosen {data[act]}, {len(data)}")
        return act

    @socketio.on("game_update")
    def get_update(data):
        print(data)

    @socketio.on("update_game_status")
    def update_game_status(data):
        # update game, get bot's response, send response
        pass

