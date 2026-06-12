"""Generated from Smithy shape ``com.amazonaws.mediastoredata#RequestedRangeNotSatisfiableException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediastore_data.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_mediastore_data.types.error_message


class RequestedRangeNotSatisfiableException_(TypedDict):
    message: NotRequired["aws_sdk_mediastore_data.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: RequestedRangeNotSatisfiableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RequestedRangeNotSatisfiableException_:
    out: RequestedRangeNotSatisfiableException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class RequestedRangeNotSatisfiableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.mediastoredata#RequestedRangeNotSatisfiableException``."""

    code: str | None = "RequestedRangeNotSatisfiableException"

    def __init__(self, data: RequestedRangeNotSatisfiableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestedRangeNotSatisfiableException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "RequestedRangeNotSatisfiableException":
        return cls(deserialize_json(data))
