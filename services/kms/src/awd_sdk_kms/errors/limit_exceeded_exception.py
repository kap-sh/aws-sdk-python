"""Generated from Smithy shape ``com.amazonaws.kms#LimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class LimitExceededException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
        )
        self.data = data
