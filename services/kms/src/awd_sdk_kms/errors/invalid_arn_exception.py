"""Generated from Smithy shape ``com.amazonaws.kms#InvalidArnException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class InvalidArnException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class InvalidArnException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#InvalidArnException``."""

    code: str | None = "InvalidArnException"

    def __init__(self, data: InvalidArnException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidArnException",
        )
        self.data = data
