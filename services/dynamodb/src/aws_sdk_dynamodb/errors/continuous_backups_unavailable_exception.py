"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContinuousBackupsUnavailableException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class ContinuousBackupsUnavailableException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class ContinuousBackupsUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#ContinuousBackupsUnavailableException``."""

    code: str | None = "ContinuousBackupsUnavailableException"

    def __init__(self, data: ContinuousBackupsUnavailableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ContinuousBackupsUnavailableException",
        )
        self.data = data
