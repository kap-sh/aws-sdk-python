"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyUriEndpointInUseException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class XksProxyUriEndpointInUseException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class XksProxyUriEndpointInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#XksProxyUriEndpointInUseException``."""

    code: str | None = "XksProxyUriEndpointInUseException"

    def __init__(self, data: XksProxyUriEndpointInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="XksProxyUriEndpointInUseException",
        )
        self.data = data
