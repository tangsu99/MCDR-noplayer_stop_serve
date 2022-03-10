import datetime
from mcdreforged.api.decorator import new_thread
from mcdreforged.plugin.server_interface import PluginServerInterface


def period_time():
    start_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '22:00', '%Y-%m-%d%H:%M')
    end_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '8:00', '%Y-%m-%d%H:%M')
    n_time = datetime.datetime.now()
    if start_time < n_time < end_time:
        return True
    else:
        return False


@new_thread("get_online")
def get_online(server: PluginServerInterface):
    api = server.get_plugin_instance('minecraft_data_api')
    data_list = api.get_server_player_list()
    if data_list[0] == 0:
        return True
    else:
        return False


def stop_server(server: PluginServerInterface):
    if period_time():
        if get_online(server):
            server.stop_exit()


def on_player_left(server: PluginServerInterface, player: str):
    stop_server(server)


def on_load(server: PluginServerInterface, prev_module):
    server.logger.info("已加载")
