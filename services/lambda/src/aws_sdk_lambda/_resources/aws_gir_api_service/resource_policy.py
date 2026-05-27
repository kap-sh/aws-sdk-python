from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aws_sdk_lambda._services.aws_gir_api_service import (
        LambdaClient,
    )
    from aws_sdk_lambda._services.async_aws_gir_api_service import (
        AsyncLambdaClient,
    )


class ResourcePolicy:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service


class AsyncResourcePolicy:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service
