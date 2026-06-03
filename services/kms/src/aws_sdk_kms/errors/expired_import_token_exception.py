"""Generated from Smithy shape ``com.amazonaws.kms#ExpiredImportTokenException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class ExpiredImportTokenException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class ExpiredImportTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#ExpiredImportTokenException``."""

    code: str | None = "ExpiredImportTokenException"

    def __init__(self, data: ExpiredImportTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExpiredImportTokenException",
        )
        self.data = data
