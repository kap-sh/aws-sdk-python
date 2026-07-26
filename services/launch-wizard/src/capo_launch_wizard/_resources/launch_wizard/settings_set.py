from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_launch_wizard._services.async_launch_wizard import (
        AsyncLaunchWizardClient,
    )
    from capo_launch_wizard._services.launch_wizard import (
        LaunchWizardClient,
    )


class SettingsSet:
    def __init__(self, service: LaunchWizardClient) -> None:
        self._service = service


class AsyncSettingsSet:
    def __init__(self, service: AsyncLaunchWizardClient) -> None:
        self._service = service
