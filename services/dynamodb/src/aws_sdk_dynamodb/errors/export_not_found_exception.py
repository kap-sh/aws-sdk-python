"""Generated from Smithy shape ``com.amazonaws.dynamodb#ExportNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class ExportNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class ExportNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ExportNotFoundException``."""

    code: str | None = "ExportNotFoundException"

    def __init__(self, data: ExportNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExportNotFoundException",
        )
        self.data = data
