"""Generated from Smithy shape ``com.amazonaws.kms#KeyUnavailableException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class KeyUnavailableException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class KeyUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#KeyUnavailableException``."""

    code: str | None = "KeyUnavailableException"

    def __init__(self, data: KeyUnavailableException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="KeyUnavailableException",
        )
        self.data = data
