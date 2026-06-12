from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aws_sdk_ssm_guiconnect._services.async_ssm_gui_connect import (
        AsyncSSMGuiConnectClient,
    )
    from aws_sdk_ssm_guiconnect._services.ssm_gui_connect import (
        SSMGuiConnectClient,
    )


class ConnectionAccess:
    def __init__(self, service: SSMGuiConnectClient) -> None:
        self._service = service


class AsyncConnectionAccess:
    def __init__(self, service: AsyncSSMGuiConnectClient) -> None:
        self._service = service
