from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aws_sdk_odb._services.async_odb import AsyncodbClient
    from aws_sdk_odb._services.odb import odbClient


class ExascaleDbStorageVaultResource:
    def __init__(self, service: odbClient) -> None:
        self._service = service


class AsyncExascaleDbStorageVaultResource:
    def __init__(self, service: AsyncodbClient) -> None:
        self._service = service
