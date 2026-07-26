from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_medical_imaging._services.async_medical_imaging import (
        AsyncMedicalImagingClient,
    )
    from capo_medical_imaging._services.medical_imaging import (
        MedicalImagingClient,
    )


class ImageSetResource:
    def __init__(self, service: MedicalImagingClient) -> None:
        self._service = service


class AsyncImageSetResource:
    def __init__(self, service: AsyncMedicalImagingClient) -> None:
        self._service = service
