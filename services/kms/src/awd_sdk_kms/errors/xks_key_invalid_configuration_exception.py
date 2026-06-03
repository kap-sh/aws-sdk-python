"""Generated from Smithy shape ``com.amazonaws.kms#XksKeyInvalidConfigurationException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class XksKeyInvalidConfigurationException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class XksKeyInvalidConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#XksKeyInvalidConfigurationException``."""

    code: str | None = "XksKeyInvalidConfigurationException"

    def __init__(self, data: XksKeyInvalidConfigurationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="XksKeyInvalidConfigurationException",
        )
        self.data = data
