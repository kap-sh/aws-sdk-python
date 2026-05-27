"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupInUseException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class BackupInUseException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class BackupInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#BackupInUseException``."""

    code: str | None = "BackupInUseException"

    def __init__(self, data: BackupInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BackupInUseException",
        )
        self.data = data
