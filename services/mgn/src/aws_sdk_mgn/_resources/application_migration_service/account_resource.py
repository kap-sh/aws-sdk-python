from typing import Optional, TYPE_CHECKING
from aws_sdk_mgn._services.async_mgn import ensure_async_iterator
from aws_sdk_mgn._services.mgn import ensure_sync_iterator
if TYPE_CHECKING:
    from aws_sdk_mgn._services.mgn import mgnClient, mgnClientConfig
    from aws_sdk_mgn._services.async_mgn import AsyncmgnClient, AsyncmgnClientConfig

class AccountResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service

class AsyncAccountResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service