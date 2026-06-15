from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aws_sdk_rtbfabric._services.async_rtb_fabric import (
        AsyncRTBFabricClient,
    )
    from aws_sdk_rtbfabric._services.rtb_fabric import (
        RTBFabricClient,
    )


class Gateway:
    def __init__(self, service: RTBFabricClient) -> None:
        self._service = service


class AsyncGateway:
    def __init__(self, service: AsyncRTBFabricClient) -> None:
        self._service = service
