from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_ssm_guiconnect._services.async_ssm_gui_connect import (
        AsyncSSMGuiConnectClient,
    )
    from capo_ssm_guiconnect._services.ssm_gui_connect import (
        SSMGuiConnectClient,
    )


class Connection:
    def __init__(self, service: SSMGuiConnectClient) -> None:
        self._service = service


class AsyncConnection:
    def __init__(self, service: AsyncSSMGuiConnectClient) -> None:
        self._service = service
