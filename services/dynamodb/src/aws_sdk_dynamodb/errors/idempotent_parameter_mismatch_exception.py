"""Generated from Smithy shape ``com.amazonaws.dynamodb#IdempotentParameterMismatchException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class IdempotentParameterMismatchException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class IdempotentParameterMismatchException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#IdempotentParameterMismatchException``."""

    code: str | None = "IdempotentParameterMismatchException"

    def __init__(self, data: IdempotentParameterMismatchException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IdempotentParameterMismatchException",
        )
        self.data = data
