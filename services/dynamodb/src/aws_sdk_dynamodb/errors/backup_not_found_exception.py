"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_dynamodb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.error_message


class BackupNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_dynamodb.types.error_message.ErrorMessage"]


class BackupNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dynamodb#BackupNotFoundException``."""

    code: str | None = "BackupNotFoundException"

    def __init__(self, data: BackupNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BackupNotFoundException",
        )
        self.data = data
