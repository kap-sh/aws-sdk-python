"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ThrottledRequestException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_socialmessaging.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.error_message


class ThrottledRequestException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_socialmessaging.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ThrottledRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottledRequestException_:
    out: ThrottledRequestException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ThrottledRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.socialmessaging#ThrottledRequestException``."""

    code: str | None = "ThrottledRequestException"

    def __init__(self, data: ThrottledRequestException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=True,
            code="ThrottledRequestException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottledRequestException":
        return cls(deserialize_json(data))
