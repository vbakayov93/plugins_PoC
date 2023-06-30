from logging import Logger
from random import randint
from time import sleep
from typing import Optional

from ...engine import PluginCore
from ...model import Meta, Dataset

class AdvanceSamplePlugin(PluginCore):

    def __init__(self, logger: Logger) -> None:
        super().__init__(logger)
        self.meta = Meta(
            name='Advanced Sample Plugin',
            description='Advanced Sample plugin template',
            version='0.0.1'
        )

    @staticmethod
    def __simulate_operation() -> None:
        sleep_duration = randint(1, 100) / 100
        sleep(sleep_duration)

    def __get_tenant_short_name(self) -> str:
        self._logger.debug('Enquiring device firmware')
        self.__simulate_operation()
        return "gtc"

    def __get_description(self) -> str:
        self._logger.debug('Enquiring messaging protocol')
        self.__simulate_operation()
        return "global dm nielsen gtc data."


    def __get_source(self) -> str:
        self._logger.debug('Enquiring source')
        self.__simulate_operation()
        return "source_gtc"

    def __get_errors(self) -> [int]:
        self._logger.debug('Enquiring errors')
        self.__simulate_operation()
        return [0x2f3a6c, 0xa8e1f5]

    def __create_dataset(self) -> Dataset:
        tenant_short_name = self.__get_tenant_short_name()
        get_description = self.__get_description()
        errors = self.__get_errors()
        source = self.__get_source()

        return Dataset(
            name='Dataset initialized by the advanced plugin',
            tenantshortname=tenant_short_name,
            source=source,
            description=get_description,
            errors=errors
        )

    def invoke(self, command: chr, protocol: Optional[str] = None) -> Dataset:
        self._logger.debug(f'Command: {command} -> {self.meta}')
        device = self.__create_dataset()
        return device

    def validate_dataset(self, str_to_validate: str) -> bool:
        self._logger.debug(f'string to validate: {str_to_validate} -> {self.meta}')
        if str_to_validate != "expected_string_in_advanced_plugin":
            return False
        return True
