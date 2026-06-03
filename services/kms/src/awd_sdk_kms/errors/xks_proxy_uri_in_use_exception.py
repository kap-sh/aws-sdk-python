"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyUriInUseException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class XksProxyUriInUseException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class XksProxyUriInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#XksProxyUriInUseException``."""

    code: str | None = "XksProxyUriInUseException"

    def __init__(self, data: XksProxyUriInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="XksProxyUriInUseException",
        )
        self.data = data
