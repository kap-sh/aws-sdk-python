from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_resiliencehubv2._services.async_resiliencehubv2 import (
        Asyncresiliencehubv2Client,
    )
    from capo_resiliencehubv2._services.resiliencehubv2 import (
        resiliencehubv2Client,
    )


class IamAppResource:
    def __init__(self, service: resiliencehubv2Client) -> None:
        self._service = service


class AsyncIamAppResource:
    def __init__(self, service: Asyncresiliencehubv2Client) -> None:
        self._service = service
