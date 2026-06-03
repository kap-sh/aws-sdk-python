"""Generated from Smithy shape ``com.amazonaws.kms#KMSInvalidStateException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class KMSInvalidStateException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class KMSInvalidStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#KMSInvalidStateException``."""

    code: str | None = "KMSInvalidStateException"

    def __init__(self, data: KMSInvalidStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSInvalidStateException",
        )
        self.data = data
