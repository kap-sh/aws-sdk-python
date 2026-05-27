"""Generated from Smithy shape ``com.amazonaws.dynamodb#DuplicateItemException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class DuplicateItemException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class DuplicateItemException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#DuplicateItemException``."""

    code: str | None = "DuplicateItemException"

    def __init__(self, data: DuplicateItemException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DuplicateItemException",
        )
        self.data = data
