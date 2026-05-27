"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class ReplicaNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class ReplicaNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ReplicaNotFoundException``."""

    code: str | None = "ReplicaNotFoundException"

    def __init__(self, data: ReplicaNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReplicaNotFoundException",
        )
        self.data = data
