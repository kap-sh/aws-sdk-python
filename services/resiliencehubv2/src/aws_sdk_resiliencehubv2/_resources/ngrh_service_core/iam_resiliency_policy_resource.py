from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aws_sdk_resiliencehubv2._services.async_resiliencehubv2 import (
        Asyncresiliencehubv2Client,
    )
    from aws_sdk_resiliencehubv2._services.resiliencehubv2 import (
        resiliencehubv2Client,
    )


class IamResiliencyPolicyResource:
    def __init__(self, service: resiliencehubv2Client) -> None:
        self._service = service


class AsyncIamResiliencyPolicyResource:
    def __init__(self, service: Asyncresiliencehubv2Client) -> None:
        self._service = service
