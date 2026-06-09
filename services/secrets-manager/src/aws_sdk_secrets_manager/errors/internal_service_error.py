"""Generated from Smithy shape ``com.amazonaws.secretsmanager#InternalServiceError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_secrets_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.error_message


class InternalServiceError_(TypedDict):
    message: NotRequired["aws_sdk_secrets_manager.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServiceError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServiceError_:
    out: InternalServiceError_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InternalServiceError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.secretsmanager#InternalServiceError``."""

    code: str | None = "InternalServiceError"

    def __init__(self, data: InternalServiceError_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServiceError",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InternalServiceError":
        return cls(deserialize_aws_json_1_1(data))
