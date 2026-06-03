"""Generated from Smithy shape ``com.amazonaws.kms#XksKeyNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class XksKeyNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class XksKeyNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#XksKeyNotFoundException``."""

    code: str | None = "XksKeyNotFoundException"

    def __init__(self, data: XksKeyNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="XksKeyNotFoundException",
        )
        self.data = data
