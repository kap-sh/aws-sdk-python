"""Generated from Smithy shape ``com.amazonaws.kms#InvalidCiphertextException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class InvalidCiphertextException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class InvalidCiphertextException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#InvalidCiphertextException``."""

    code: str | None = "InvalidCiphertextException"

    def __init__(self, data: InvalidCiphertextException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidCiphertextException",
        )
        self.data = data
