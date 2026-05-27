"""Generated from Smithy shape ``com.amazonaws.dynamodb#IndexNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class IndexNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class IndexNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#IndexNotFoundException``."""

    code: str | None = "IndexNotFoundException"

    def __init__(self, data: IndexNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IndexNotFoundException",
        )
        self.data = data
