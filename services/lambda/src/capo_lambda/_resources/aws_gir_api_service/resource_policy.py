from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_lambda._services._lambda import LambdaClient
    from capo_lambda._services.async__lambda import (
        AsyncLambdaClient,
    )


class ResourcePolicy:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service


class AsyncResourcePolicy:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service
