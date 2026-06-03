"""Generated from Smithy shape ``com.amazonaws.kms#CloudHsmClusterNotActiveException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class CloudHsmClusterNotActiveException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class CloudHsmClusterNotActiveException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#CloudHsmClusterNotActiveException``."""

    code: str | None = "CloudHsmClusterNotActiveException"

    def __init__(self, data: CloudHsmClusterNotActiveException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmClusterNotActiveException",
        )
        self.data = data
