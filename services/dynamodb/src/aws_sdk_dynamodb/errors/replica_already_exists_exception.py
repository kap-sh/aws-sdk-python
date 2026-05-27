"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicaAlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class ReplicaAlreadyExistsException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class ReplicaAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ReplicaAlreadyExistsException``."""

    code: str | None = "ReplicaAlreadyExistsException"

    def __init__(self, data: ReplicaAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReplicaAlreadyExistsException",
        )
        self.data = data
