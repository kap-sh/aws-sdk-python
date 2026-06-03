"""Generated from Smithy shape ``com.amazonaws.kms#KMSInvalidSignatureException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class KMSInvalidSignatureException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class KMSInvalidSignatureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#KMSInvalidSignatureException``."""

    code: str | None = "KMSInvalidSignatureException"

    def __init__(self, data: KMSInvalidSignatureException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSInvalidSignatureException",
        )
        self.data = data
