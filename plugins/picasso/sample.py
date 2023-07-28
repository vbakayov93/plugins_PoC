from logging import Logger
from typing import Optional

from pyspark.pandas import DataFrame

from ...api import PluginAPI
from ...model import Meta, Dataset


class PicassoPlugin(PluginAPI):

    def __init__(self, logger: Logger) -> None:
        super().__init__(logger)
        self.meta = Meta(
            name='Picasso Plugin',
            description='Picasso plugin template',
            version='0.0.1'
        )

    def __create_dataset(self) -> Dataset:
        return Dataset(
            name='Dataset initialized by the picasso plugin',
            tenantshortname="sap_x40",
            source="source_sap",
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
        if str_to_validate != "expected_string_in_picasso_plugin":
            return False
        return True

    def bronze_to_silver_data_enrichment(self, df: DataFrame) -> DataFrame:
        return df.head(10)
