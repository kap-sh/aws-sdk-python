from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_mgn._services.async_mgn import AsyncmgnClient
    from capo_mgn._services.mgn import mgnClient


class AccountResource:
    def __init__(self, service: mgnClient) -> None:
        self._service = service


class AsyncAccountResource:
    def __init__(self, service: AsyncmgnClient) -> None:
        self._service = service
