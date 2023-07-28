from logging import Logger
from typing import Optional

from pyspark.pandas import DataFrame

from ...api import PluginCore
from ...model import Meta, Dataset


class SamplePlugin(PluginCore):

    def __init__(self, logger: Logger) -> None:
        super().__init__(logger)
        self.meta = Meta(
            name='Sample Plugin',
            description='Sample plugin template',
            version='0.0.1'
        )

    def __create_dataset(self) -> Dataset:
        return Dataset(
            name='Dataset initialized by the advanced plugin',
            tenantshortname="sap_x40",
            source="source_sap",
            description="sap description goes here",
            errors=[0x0000]
        )

    def invoke(self, command: chr, protocol: Optional[str] = None) -> Dataset:
        self._logger.debug(f'Command: {command} -> {self.meta}')
        device = self.__create_dataset()
        return device

    def validate_dataset(self, str_to_validate: str) -> bool:
        self._logger.debug(f'string to validate: {str_to_validate} -> {self.meta}')
        if str_to_validate != "expected_string_in_sample_plugin":
            return False
        return True

    def pass_df_to_plugin(self, df: DataFrame) -> DataFrame:
        return df.head(10)

    def implement_by_only_one_plugin(self):
        return "OK"
