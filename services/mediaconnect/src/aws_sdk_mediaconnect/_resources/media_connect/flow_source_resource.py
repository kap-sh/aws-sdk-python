from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aws_sdk_mediaconnect._services.async_media_connect import (
        AsyncMediaConnectClient,
    )
    from aws_sdk_mediaconnect._services.media_connect import (
        MediaConnectClient,
    )


class FlowSourceResource:
    def __init__(self, service: MediaConnectClient) -> None:
        self._service = service


class AsyncFlowSourceResource:
    def __init__(self, service: AsyncMediaConnectClient) -> None:
        self._service = service
