"""Generated from Smithy shape ``com.amazonaws.kms#CloudHsmClusterNotRelatedException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class CloudHsmClusterNotRelatedException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class CloudHsmClusterNotRelatedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#CloudHsmClusterNotRelatedException``."""

    code: str | None = "CloudHsmClusterNotRelatedException"

    def __init__(self, data: CloudHsmClusterNotRelatedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmClusterNotRelatedException",
        )
        self.data = data
