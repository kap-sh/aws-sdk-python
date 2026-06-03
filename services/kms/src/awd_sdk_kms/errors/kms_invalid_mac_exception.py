"""Generated from Smithy shape ``com.amazonaws.kms#KMSInvalidMacException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class KMSInvalidMacException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class KMSInvalidMacException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#KMSInvalidMacException``."""

    code: str | None = "KMSInvalidMacException"

    def __init__(self, data: KMSInvalidMacException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSInvalidMacException",
        )
        self.data = data
