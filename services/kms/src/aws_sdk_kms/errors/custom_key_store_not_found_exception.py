"""Generated from Smithy shape ``com.amazonaws.kms#CustomKeyStoreNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class CustomKeyStoreNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class CustomKeyStoreNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#CustomKeyStoreNotFoundException``."""

    code: str | None = "CustomKeyStoreNotFoundException"

    def __init__(self, data: CustomKeyStoreNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CustomKeyStoreNotFoundException",
        )
        self.data = data
