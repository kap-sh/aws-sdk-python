"""Generated from Smithy shape ``com.amazonaws.kms#DryRunOperationException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_kms.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_kms.types.error_message_type


class DryRunOperationException_(TypedDict):
    message: NotRequired["aws_sdk_kms.types.error_message_type.ErrorMessageType"]


class DryRunOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#DryRunOperationException``."""

    code: str | None = "DryRunOperationException"

    def __init__(self, data: DryRunOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DryRunOperationException",
        )
        self.data = data
