"""Generated from Smithy shape ``com.amazonaws.kms#IncorrectKeyMaterialException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from awd_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import awd_sdk_kms.types.error_message_type


class IncorrectKeyMaterialException_(TypedDict):
    message: NotRequired["awd_sdk_kms.types.error_message_type.ErrorMessageType"]


class IncorrectKeyMaterialException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#IncorrectKeyMaterialException``."""

    code: str | None = "IncorrectKeyMaterialException"

    def __init__(self, data: IncorrectKeyMaterialException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncorrectKeyMaterialException",
        )
        self.data = data
