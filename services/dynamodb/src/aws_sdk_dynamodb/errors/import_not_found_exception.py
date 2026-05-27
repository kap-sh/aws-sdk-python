"""Generated from Smithy shape ``com.amazonaws.dynamodb#ImportNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class ImportNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class ImportNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ImportNotFoundException``."""

    code: str | None = "ImportNotFoundException"

    def __init__(self, data: ImportNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ImportNotFoundException",
        )
        self.data = data
