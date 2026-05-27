"""Generated from Smithy shape ``com.amazonaws.dynamodb#InvalidRestoreTimeException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class InvalidRestoreTimeException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class InvalidRestoreTimeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#InvalidRestoreTimeException``."""

    code: str | None = "InvalidRestoreTimeException"

    def __init__(self, data: InvalidRestoreTimeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRestoreTimeException",
        )
        self.data = data
