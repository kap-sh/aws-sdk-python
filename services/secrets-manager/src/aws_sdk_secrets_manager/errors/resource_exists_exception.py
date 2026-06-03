"""Generated from Smithy shape ``com.amazonaws.secretsmanager#ResourceExistsException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_secrets_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.error_message


class ResourceExistsException_(TypedDict):
    message: NotRequired["aws_sdk_secrets_manager.types.error_message.ErrorMessage"]


class ResourceExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.secretsmanager#ResourceExistsException``."""

    code: str | None = "ResourceExistsException"

    def __init__(self, data: ResourceExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceExistsException",
        )
        self.data = data
