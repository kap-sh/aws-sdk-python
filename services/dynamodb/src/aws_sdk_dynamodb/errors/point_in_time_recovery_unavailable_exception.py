"""Generated from Smithy shape ``com.amazonaws.dynamodb#PointInTimeRecoveryUnavailableException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class PointInTimeRecoveryUnavailableException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class PointInTimeRecoveryUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#PointInTimeRecoveryUnavailableException``."""

    code: str | None = "PointInTimeRecoveryUnavailableException"

    def __init__(self, data: PointInTimeRecoveryUnavailableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PointInTimeRecoveryUnavailableException",
        )
        self.data = data
