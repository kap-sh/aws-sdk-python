"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyUriUnreachableException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class XksProxyUriUnreachableException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class XksProxyUriUnreachableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#XksProxyUriUnreachableException``."""

    code: str | None = "XksProxyUriUnreachableException"

    def __init__(self, data: XksProxyUriUnreachableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="XksProxyUriUnreachableException",
        )
        self.data = data
