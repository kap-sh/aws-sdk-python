"""Generated from Smithy shape ``com.amazonaws.dynamodb#TableAlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class TableAlreadyExistsException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class TableAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#TableAlreadyExistsException``."""

    code: str | None = "TableAlreadyExistsException"

    def __init__(self, data: TableAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TableAlreadyExistsException",
        )
        self.data = data
