"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableAlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class GlobalTableAlreadyExistsException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class GlobalTableAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#GlobalTableAlreadyExistsException``."""

    code: str | None = "GlobalTableAlreadyExistsException"

    def __init__(self, data: GlobalTableAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GlobalTableAlreadyExistsException",
        )
        self.data = data
