"""Generated from Smithy shape ``com.amazonaws.kms#KMSInternalException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kms.errors import ServiceError

if TYPE_CHECKING:
    import capo_kms.types.error_message_type


class KMSInternalException_(TypedDict, closed=True):
    message: NotRequired["capo_kms.types.error_message_type.ErrorMessageType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KMSInternalException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KMSInternalException_:
    out: KMSInternalException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class KMSInternalException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.kms#KMSInternalException``."""

    code: str | None = "KMSInternalException"

    def __init__(self, data: KMSInternalException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="KMSInternalException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "KMSInternalException":
        return cls(deserialize_aws_json_1_1(data))
