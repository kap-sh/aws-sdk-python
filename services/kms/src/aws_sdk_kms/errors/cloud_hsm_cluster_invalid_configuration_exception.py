"""Generated from Smithy shape ``com.amazonaws.kms#CloudHsmClusterInvalidConfigurationException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class CloudHsmClusterInvalidConfigurationException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class CloudHsmClusterInvalidConfigurationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#CloudHsmClusterInvalidConfigurationException``."""

    code: str | None = "CloudHsmClusterInvalidConfigurationException"

    def __init__(self, data: CloudHsmClusterInvalidConfigurationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmClusterInvalidConfigurationException",
        )
        self.data = data
