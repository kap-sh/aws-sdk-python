"""Generated from Smithy shape ``com.amazonaws.detective#TooManyRequestsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_detective.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_detective.types.error_message


class TooManyRequestsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_detective.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: TooManyRequestsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> TooManyRequestsException_:
    out: TooManyRequestsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TooManyRequestsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.detective#TooManyRequestsException``."""

    code: str | None = "TooManyRequestsException"

    def __init__(self, data: TooManyRequestsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyRequestsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "TooManyRequestsException":
        return cls(deserialize_json(data))
