"""Generated from Smithy shape ``com.amazonaws.dynamodb#GlobalTableNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class GlobalTableNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class GlobalTableNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#GlobalTableNotFoundException``."""

    code: str | None = "GlobalTableNotFoundException"

    def __init__(self, data: GlobalTableNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="GlobalTableNotFoundException",
        )
        self.data = data
