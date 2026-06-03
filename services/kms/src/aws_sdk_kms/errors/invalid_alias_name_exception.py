"""Generated from Smithy shape ``com.amazonaws.kms#InvalidAliasNameException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class InvalidAliasNameException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class InvalidAliasNameException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#InvalidAliasNameException``."""

    code: str | None = "InvalidAliasNameException"

    def __init__(self, data: InvalidAliasNameException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidAliasNameException",
        )
        self.data = data
