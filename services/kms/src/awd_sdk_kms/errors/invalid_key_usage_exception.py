"""Generated from Smithy shape ``com.amazonaws.kms#InvalidKeyUsageException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class InvalidKeyUsageException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class InvalidKeyUsageException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#InvalidKeyUsageException``."""

    code: str | None = "InvalidKeyUsageException"

    def __init__(self, data: InvalidKeyUsageException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidKeyUsageException",
        )
        self.data = data
