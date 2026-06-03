"""Generated from Smithy shape ``com.amazonaws.secretsmanager#EncryptionFailure``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_secrets_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.error_message


class EncryptionFailure_(TypedDict):
    message: NotRequired["aws_sdk_secrets_manager.types.error_message.ErrorMessage"]


class EncryptionFailure(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.secretsmanager#EncryptionFailure``."""

    code: str | None = "EncryptionFailure"

    def __init__(self, data: EncryptionFailure_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EncryptionFailure",
        )
        self.data = data
