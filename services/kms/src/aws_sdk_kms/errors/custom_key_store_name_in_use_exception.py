"""Generated from Smithy shape ``com.amazonaws.kms#CustomKeyStoreNameInUseException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class CustomKeyStoreNameInUseException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class CustomKeyStoreNameInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#CustomKeyStoreNameInUseException``."""

    code: str | None = "CustomKeyStoreNameInUseException"

    def __init__(self, data: CustomKeyStoreNameInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomKeyStoreNameInUseException",
        )
        self.data = data
