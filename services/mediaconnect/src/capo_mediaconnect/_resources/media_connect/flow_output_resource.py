from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
    )
    from capo_mediaconnect._services.media_connect import (
        MediaConnectClient,
    )


class FlowOutputResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service


class AsyncFlowOutputResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service
