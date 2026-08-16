"""Generated from Smithy shape ``com.amazonaws.kms#KeyUnavailableException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import ServiceError

if TYPE_CHECKING:
    import capo_kms.types.error_message_type


class KeyUnavailableException_(TypedDict, closed=True):
    message: NotRequired["capo_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KeyUnavailableException_:
    out: KeyUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KeyUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#KeyUnavailableException``."""

    code: str | None = "KeyUnavailableException"

    def __init__(self, data: KeyUnavailableException_, message: str | None = None):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="KeyUnavailableException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "KeyUnavailableException":
        return cls(deserialize_aws_json_1_1(data), message)
