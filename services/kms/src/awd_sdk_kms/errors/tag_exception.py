"""Generated from Smithy shape ``com.amazonaws.kms#TagException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class TagException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class TagException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#TagException``."""

    code: str | None = "TagException"

    def __init__(self, data: TagException_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="TagException"
        )
        self.data = data
