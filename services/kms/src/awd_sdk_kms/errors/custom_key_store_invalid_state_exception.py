"""Generated from Smithy shape ``com.amazonaws.kms#CustomKeyStoreInvalidStateException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class CustomKeyStoreInvalidStateException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class CustomKeyStoreInvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#CustomKeyStoreInvalidStateException``."""

    code: str | None = "CustomKeyStoreInvalidStateException"

    def __init__(self, data: CustomKeyStoreInvalidStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomKeyStoreInvalidStateException",
        )
        self.data = data
