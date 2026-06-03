"""Generated from Smithy shape ``com.amazonaws.kms#KMSInternalException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class KMSInternalException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class KMSInternalException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#KMSInternalException``."""

    code: str | None = "KMSInternalException"

    def __init__(self, data: KMSInternalException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSInternalException",
        )
        self.data = data
