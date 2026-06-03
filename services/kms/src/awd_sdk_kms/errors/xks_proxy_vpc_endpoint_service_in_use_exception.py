"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyVpcEndpointServiceInUseException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class XksProxyVpcEndpointServiceInUseException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class XksProxyVpcEndpointServiceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#XksProxyVpcEndpointServiceInUseException``."""

    code: str | None = "XksProxyVpcEndpointServiceInUseException"

    def __init__(self, data: XksProxyVpcEndpointServiceInUseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="XksProxyVpcEndpointServiceInUseException",
        )
        self.data = data
