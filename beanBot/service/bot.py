import nonebot
from os import path

import beanBot.settings.base as base


class Bot:

    def __init__(self) -> None:
        pass

    def run(self):
        nonebot.init(base)
        # 导入插件
        for plugin in base.PLUGINS:
            nonebot.load_plugins(
                path.join(path.dirname(__file__), 'beanBot', 'plugins', plugin),
                f'beanBot.plugins.{plugin}'
            )
        nonebot.run()