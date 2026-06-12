from typing import Optional, TYPE_CHECKING
from aws_sdk_drs._services.async_drs import ensure_async_iterator
from aws_sdk_drs._services.drs import ensure_sync_iterator
if TYPE_CHECKING:
    from aws_sdk_drs._services.drs import drsClient, drsClientConfig
    from aws_sdk_drs._services.async_drs import AsyncdrsClient, AsyncdrsClientConfig

class AccountResource:
    def __init__(self, service: drsClient) -> None:
        self._service = service

class AsyncAccountResource:
    def __init__(self, service: AsyncdrsClient) -> None:
        self._service = service