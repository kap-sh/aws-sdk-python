from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aws_sdk_drs._services.async_drs import AsyncdrsClient
    from aws_sdk_drs._services.drs import drsClient


class AccountResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service


class AsyncAccountResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service
