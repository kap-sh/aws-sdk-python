"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyVpcEndpointServiceInvalidConfigurationException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class XksProxyVpcEndpointServiceInvalidConfigurationException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class XksProxyVpcEndpointServiceInvalidConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#XksProxyVpcEndpointServiceInvalidConfigurationException``."""

    code: str | None = "XksProxyVpcEndpointServiceInvalidConfigurationException"

    def __init__(self, data: XksProxyVpcEndpointServiceInvalidConfigurationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="XksProxyVpcEndpointServiceInvalidConfigurationException",
        )
        self.data = data
