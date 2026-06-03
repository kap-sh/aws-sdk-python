"""Generated from Smithy shape ``com.amazonaws.kms#CloudHsmClusterNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class CloudHsmClusterNotFoundException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class CloudHsmClusterNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#CloudHsmClusterNotFoundException``."""

    code: str | None = "CloudHsmClusterNotFoundException"

    def __init__(self, data: CloudHsmClusterNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CloudHsmClusterNotFoundException",
        )
        self.data = data
