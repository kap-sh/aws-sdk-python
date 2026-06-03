"""Generated from Smithy shape ``com.amazonaws.kms#InvalidImportTokenException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class InvalidImportTokenException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class InvalidImportTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#InvalidImportTokenException``."""

    code: str | None = "InvalidImportTokenException"

    def __init__(self, data: InvalidImportTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidImportTokenException",
        )
        self.data = data
