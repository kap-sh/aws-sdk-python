"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class TableNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class TableNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#TableNotFoundException``."""

    code: str | None = "TableNotFoundException"

    def __init__(self, data: TableNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TableNotFoundException",
        )
        self.data = data
