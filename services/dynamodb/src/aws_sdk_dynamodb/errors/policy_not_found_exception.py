"""Generated from Smithy shape ``com.amazonaws.dynamodb#PolicyNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class PolicyNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class PolicyNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#PolicyNotFoundException``."""

    code: str | None = "PolicyNotFoundException"

    def __init__(self, data: PolicyNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyNotFoundException",
        )
        self.data = data
