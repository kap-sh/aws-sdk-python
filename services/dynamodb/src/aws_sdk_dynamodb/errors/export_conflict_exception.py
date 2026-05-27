"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportConflictException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class ExportConflictException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class ExportConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ExportConflictException``."""

    code: str | None = "ExportConflictException"

    def __init__(self, data: ExportConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExportConflictException",
        )
        self.data = data
