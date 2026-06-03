"""Generated from Smithy shape ``com.amazonaws.kms#InvalidMarkerException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class InvalidMarkerException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class InvalidMarkerException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#InvalidMarkerException``."""

    code: str | None = "InvalidMarkerException"

    def __init__(self, data: InvalidMarkerException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidMarkerException",
        )
        self.data = data
