from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_artifact._services.artifact import ArtifactClient
    from capo_artifact._services.async_artifact import (
        AsyncArtifactClient,
    )


class TermResource:
    def __init__(self, service: ArtifactClient) -> None:
        self._service = service


class AsyncTermResource:
    def __init__(self, service: AsyncArtifactClient) -> None:
        self._service = service
