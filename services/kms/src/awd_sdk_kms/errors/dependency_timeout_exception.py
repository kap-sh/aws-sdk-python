"""Generated from Smithy shape ``com.amazonaws.kms#DependencyTimeoutException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class DependencyTimeoutException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class DependencyTimeoutException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#DependencyTimeoutException``."""

    code: str | None = "DependencyTimeoutException"

    def __init__(self, data: DependencyTimeoutException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyTimeoutException",
        )
        self.data = data
