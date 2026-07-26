from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_arc_zonal_shift._services.arc_zonal_shift import (
        ARCZonalShiftClient,
    )
    from capo_arc_zonal_shift._services.async_arc_zonal_shift import (
        AsyncARCZonalShiftClient,
    )


class AutoshiftTriggerResource:
    def __init__(self, service: ARCZonalShiftClient) -> None:
        self._service = service


class AsyncAutoshiftTriggerResource:
    def __init__(self, service: AsyncARCZonalShiftClient) -> None:
        self._service = service
