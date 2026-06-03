"""Generated from Smithy shape ``com.amazonaws.kms#XksKeyAlreadyInUseException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class XksKeyAlreadyInUseException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class XksKeyAlreadyInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#XksKeyAlreadyInUseException``."""

    code: str | None = "XksKeyAlreadyInUseException"

    def __init__(self, data: XksKeyAlreadyInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="XksKeyAlreadyInUseException",
        )
        self.data = data
