"""Generated from Smithy shape ``com.amazonaws.secretsmanager#EncryptionFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_secrets_manager.errors import ServiceError

if TYPE_CHECKING:
    import capo_secrets_manager.types.error_message


class EncryptionFailure_(TypedDict, closed=True):
    message: NotRequired["capo_secrets_manager.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionFailure_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionFailure_:
    out: EncryptionFailure_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EncryptionFailure(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.secretsmanager#EncryptionFailure``."""

    code: str | None = "EncryptionFailure"

    def __init__(self, data: EncryptionFailure_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EncryptionFailure",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EncryptionFailure":
        return cls(deserialize_aws_json_1_1(data))
