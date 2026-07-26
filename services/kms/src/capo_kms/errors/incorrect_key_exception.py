"""Generated from Smithy shape ``com.amazonaws.kms#IncorrectKeyException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import ServiceError

if TYPE_CHECKING:
    import capo_kms.types.error_message_type


class IncorrectKeyException_(TypedDict, closed=True):
    message: NotRequired["capo_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncorrectKeyException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IncorrectKeyException_:
    out: IncorrectKeyException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class IncorrectKeyException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#IncorrectKeyException``."""

    code: str | None = "IncorrectKeyException"

    def __init__(self, data: IncorrectKeyException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IncorrectKeyException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "IncorrectKeyException":
        return cls(deserialize_aws_json_1_1(data))
