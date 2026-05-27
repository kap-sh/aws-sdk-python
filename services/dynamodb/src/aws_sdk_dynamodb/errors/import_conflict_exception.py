"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportConflictException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class ImportConflictException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class ImportConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ImportConflictException``."""

    code: str | None = "ImportConflictException"

    def __init__(self, data: ImportConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ImportConflictException",
        )
        self.data = data
