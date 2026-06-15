from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aws_sdk_mgn._services.async_mgn import AsyncmgnClient
    from aws_sdk_mgn._services.mgn import mgnClient


class ApplianceResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service


class AsyncApplianceResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service
