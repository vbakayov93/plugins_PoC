from logging import Logger
from typing import Optional, List



class IPluginRegistry(type):
    plugin_registries: List[type] = list()

    def __init__(cls, name, bases, attrs):
        super().__init__(cls)
        if name != 'PluginCore':
            IPluginRegistry.plugin_registries.append(cls)


class PluginCore(object, metaclass=IPluginRegistry):
    """
    Plugin core class
    """

    meta: Optional[Meta]

    def __init__(self, logger: Logger) -> None:
        """
        Entry init block for pluginss
        :param logger: logger that pluginss can make use of
        """
        self._logger = logger

    def invoke(self, **args) -> Dataset:
        """
        Starts main plugin flow
        :param args: possible arguments for the plugin
        :return: a dataset for the plugin
        """
        pass

    def clean_dataset(self, **args) -> Dataset:
        """
        Starts main plugin flow
        :param args: possible arguments for the plugin
        :return: a device for the plugin
        """
        pass

    def validate_dataset(self, **args) -> bool:
        """
        Starts main plugin flow
        :param args: possible arguments for the plugin
        :return: a device for the plugin
        """
        print("Apply before plugins")
        pass
