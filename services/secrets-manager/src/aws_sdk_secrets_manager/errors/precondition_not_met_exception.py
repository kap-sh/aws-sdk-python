"""Generated from Smithy shape ``com.amazonaws.secretsmanager#PreconditionNotMetException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_secrets_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.error_message


class PreconditionNotMetException_(TypedDict):
    message: NotRequired["aws_sdk_secrets_manager.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreconditionNotMetException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PreconditionNotMetException_:
    out: PreconditionNotMetException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class PreconditionNotMetException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.secretsmanager#PreconditionNotMetException``."""

    code: str | None = "PreconditionNotMetException"

    def __init__(self, data: PreconditionNotMetException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PreconditionNotMetException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PreconditionNotMetException":
        return cls(deserialize_aws_json_1_1(data))
