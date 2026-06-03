"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyInvalidConfigurationException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class XksProxyInvalidConfigurationException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class XksProxyInvalidConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#XksProxyInvalidConfigurationException``."""

    code: str | None = "XksProxyInvalidConfigurationException"

    def __init__(self, data: XksProxyInvalidConfigurationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="XksProxyInvalidConfigurationException",
        )
        self.data = data
