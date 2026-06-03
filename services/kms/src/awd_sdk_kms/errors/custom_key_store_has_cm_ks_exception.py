"""Generated from Smithy shape ``com.amazonaws.kms#CustomKeyStoreHasCMKsException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class CustomKeyStoreHasCMKsException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class CustomKeyStoreHasCMKsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#CustomKeyStoreHasCMKsException``."""

    code: str | None = "CustomKeyStoreHasCMKsException"

    def __init__(self, data: CustomKeyStoreHasCMKsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomKeyStoreHasCMKsException",
        )
        self.data = data
