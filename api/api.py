from logging import Logger
from typing import Optional, List, Any

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

    def bronze_to_silver_data_enrichment(self, **args) -> DataFrame:
        """
        Starts main plugin flow
        :param args: possible arguments for the plugin
        :return: a dataset for the plugin
        """
        pass

    def silver_to_gold_data_enrichment(self, **args) -> DataFrame:
        """
        Starts main plugin flow
        :param args: possible arguments for the plugin
        :return: a dataset for the plugin
        """
        pass

    def validate_data(self, **args) -> bool:
        """
        Starts main plugin flow
        :param args: possible arguments for the plugin
        :return: a device for the plugin
        """
        pass

    def archive_data(self, **args):
        """
        Starts main plugin flow
        :param args: possible arguments for the plugin
        :return: a device for the plugin
        """
        pass

    def partition(self, **args):
        """
        Starts main plugin flow
        :param args: possible arguments for the plugin
        :return: a device for the plugin
        """
        pass

    def encryption(self, **args):
        """
        Starts main plugin flow
        :param args: possible arguments for the plugin
        :return: a device for the plugin
        """
        pass

    def run_integrity_tests(self, **args):
        """
        Starts main plugin flow
        :param args: possible arguments for the plugin
        :return: a device for the plugin
        """
        pass