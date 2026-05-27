"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactionConflictException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class TransactionConflictException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class TransactionConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#TransactionConflictException``."""

    code: str | None = "TransactionConflictException"

    def __init__(self, data: TransactionConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TransactionConflictException",
        )
        self.data = data
