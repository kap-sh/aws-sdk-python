"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyInvalidResponseException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class XksProxyInvalidResponseException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class XksProxyInvalidResponseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#XksProxyInvalidResponseException``."""

    code: str | None = "XksProxyInvalidResponseException"

    def __init__(self, data: XksProxyInvalidResponseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="XksProxyInvalidResponseException",
        )
        self.data = data
