"""Generated from Smithy shape ``com.amazonaws.dynamodb#InvalidExportTimeException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class InvalidExportTimeException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class InvalidExportTimeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#InvalidExportTimeException``."""

    code: str | None = "InvalidExportTimeException"

    def __init__(self, data: InvalidExportTimeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidExportTimeException",
        )
        self.data = data
