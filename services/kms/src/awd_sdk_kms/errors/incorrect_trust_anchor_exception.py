"""Generated from Smithy shape ``com.amazonaws.kms#IncorrectTrustAnchorException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class IncorrectTrustAnchorException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class IncorrectTrustAnchorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#IncorrectTrustAnchorException``."""

    code: str | None = "IncorrectTrustAnchorException"

    def __init__(self, data: IncorrectTrustAnchorException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncorrectTrustAnchorException",
        )
        self.data = data
