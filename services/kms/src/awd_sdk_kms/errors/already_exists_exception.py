"""Generated from Smithy shape ``com.amazonaws.kms#AlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class AlreadyExistsException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class AlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#AlreadyExistsException``."""

    code: str | None = "AlreadyExistsException"

    def __init__(self, data: AlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AlreadyExistsException",
        )
        self.data = data
