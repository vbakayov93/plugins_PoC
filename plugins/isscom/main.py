from logging import Logger
from random import randint
from time import sleep
from typing import Optional, List

from pyspark import Row
from pyspark.sql import DataFrame

from ...api import PluginAPI
from ...model import Meta, Dataset


class IsscomPlugin(PluginAPI):

    def __init__(self, logger: Logger) -> None:
        super().__init__(logger)
        self.meta = Meta(
            name='Isscom Plugin',
            description='Isscom description goes here',
            version='0.0.1'
        )

    def __create_dataset(self) -> Dataset:
        return Dataset(
            name='Dataset initialized by the isscom plugin',
            tenantshortname="picasso",
            source="source_picasso",
            description="Picasso description goes here",
            errors=[0x0000]
        )

    # Showcase
    def invoke(self, command: chr, protocol: Optional[str] = None) -> Dataset:
        self._logger.debug(f'Command: {command} -> {self.meta}')
        device = self.__create_dataset()
        return device

    def validate_data(self, str_to_validate: str) -> bool:
        self._logger.debug(f'string to validate: {str_to_validate} -> {self.meta}')
        if str_to_validate != "expected_string_in_isscom_plugin":
            return False
        return True

    def bronze_to_silver_data_enrichment(self, df: DataFrame) -> list[Row]:
        return df.head(15)

    def silver_to_gold_data_enrichment(self, df: DataFrame) -> list[Row]:
        return df.head(5)
