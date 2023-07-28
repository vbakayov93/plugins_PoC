from logging import Logger
from typing import Optional, List

from pyspark import Row
from pyspark.sql.dataframe import DataFrame

from ..model import Meta, Dataset


class IPluginRegistry(type):
    plugin_registries: List[type] = list()

    def __init__(cls, name, bases, attrs):
        super().__init__(cls)
        if name != 'PluginAPI':
            IPluginRegistry.plugin_registries.append(cls)


class PluginAPI(object, metaclass=IPluginRegistry):
    """
    Plugin API class
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

    def validate_dataset(self, **args) -> bool:
        """
        Starts main plugin flow
        :param args: possible arguments for the plugin
        :return: a device for the plugin
        """
        pass

    def pass_df_to_plugin(self, **args) -> list[Row]:
        pass

    def implement_by_only_one_plugin(self, **args) -> bool:
        pass

