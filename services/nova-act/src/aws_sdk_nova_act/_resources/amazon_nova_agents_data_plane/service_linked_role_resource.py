from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aws_sdk_nova_act._services.async_nova_act import (
        AsyncNovaActClient,
    )
    from aws_sdk_nova_act._services.nova_act import NovaActClient


class ServiceLinkedRoleResource:
    def __init__(self, service: NovaActClient) -> None:
        self._service = service


class AsyncServiceLinkedRoleResource:
    def __init__(self, service: AsyncNovaActClient) -> None:
        self._service = service
