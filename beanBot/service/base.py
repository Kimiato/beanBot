import os

class Plugin:

    def __init__(self, name=None, default_enable=False,) -> None:
        self.name = self._get_plugin_name(name)
        self.default_enable = default_enable

    def _get_plugin_name(self, name):
        '''如果提供的name为None, 则以文件所在的目录名为名字'''
        if name == None:
            path = os.path.dirname(__file__)
            plugin_name = os.path.basename(path)
            return plugin_name
        return name
