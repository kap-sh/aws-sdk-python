"""Generated from Smithy shape ``com.amazonaws.codeconnections#UnsupportedOperationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codeconnections.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.error_message


class UnsupportedOperationException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codeconnections.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UnsupportedOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UnsupportedOperationException_:
    out: UnsupportedOperationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codeconnections#UnsupportedOperationException``."""

    code: str | None = "UnsupportedOperationException"

    def __init__(self, data: UnsupportedOperationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedOperationException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "UnsupportedOperationException":
        return cls(deserialize_aws_json_1_0(data))
