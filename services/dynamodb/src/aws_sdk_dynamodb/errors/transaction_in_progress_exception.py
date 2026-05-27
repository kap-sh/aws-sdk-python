"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactionInProgressException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class TransactionInProgressException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class TransactionInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#TransactionInProgressException``."""

    code: str | None = "TransactionInProgressException"

    def __init__(self, data: TransactionInProgressException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TransactionInProgressException",
        )
        self.data = data
