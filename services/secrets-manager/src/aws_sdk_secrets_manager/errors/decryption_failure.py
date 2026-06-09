"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DecryptionFailure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_secrets_manager.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.error_message


class DecryptionFailure_(TypedDict):
    message: NotRequired["aws_sdk_secrets_manager.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DecryptionFailure_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DecryptionFailure_:
    out: DecryptionFailure_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DecryptionFailure(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.secretsmanager#DecryptionFailure``."""

    code: str | None = "DecryptionFailure"

    def __init__(self, data: DecryptionFailure_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DecryptionFailure",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DecryptionFailure":
        return cls(deserialize_aws_json_1_1(data))
