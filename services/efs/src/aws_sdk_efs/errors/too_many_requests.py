"""Generated from Smithy shape ``com.amazonaws.efs#TooManyRequests``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_efs.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_efs.types.error_code
    import aws_sdk_efs.types.error_message


class TooManyRequests_(TypedDict):
    error_code: "aws_sdk_efs.types.error_code.ErrorCode"
    message: NotRequired["aws_sdk_efs.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequests_) -> dict:
    out: dict = {}
    out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyRequests_:
    out: TooManyRequests_ = {}  # type: ignore[typeddict-item]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError("TooManyRequests_.error_code required")
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TooManyRequests(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.efs#TooManyRequests``."""

    code: str | None = "TooManyRequests"

    def __init__(self, data: TooManyRequests_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyRequests",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TooManyRequests":
        return cls(deserialize_json(data))
