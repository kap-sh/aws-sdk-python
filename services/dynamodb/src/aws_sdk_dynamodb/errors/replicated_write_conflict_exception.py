"""Generated from Smithy shape ``com.amazonaws.dynamodb#ReplicatedWriteConflictException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class ReplicatedWriteConflictException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class ReplicatedWriteConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ReplicatedWriteConflictException``."""

    code: str | None = "ReplicatedWriteConflictException"

    def __init__(self, data: ReplicatedWriteConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="ReplicatedWriteConflictException",
        )
        self.data = data
