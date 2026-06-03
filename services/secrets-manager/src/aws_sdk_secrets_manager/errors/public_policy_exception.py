"""Generated from Smithy shape ``com.amazonaws.secretsmanager#PublicPolicyException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_secrets_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.error_message


class PublicPolicyException_(TypedDict):
    message: NotRequired["aws_sdk_secrets_manager.types.error_message.ErrorMessage"]


class PublicPolicyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.secretsmanager#PublicPolicyException``."""

    code: str | None = "PublicPolicyException"

    def __init__(self, data: PublicPolicyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PublicPolicyException",
        )
        self.data = data
