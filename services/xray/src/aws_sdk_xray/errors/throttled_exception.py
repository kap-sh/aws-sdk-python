"""Generated from Smithy shape ``com.amazonaws.xray#ThrottledException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_xray.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_xray.types.error_message


class ThrottledException_(TypedDict):
    message: NotRequired["aws_sdk_xray.types.error_message.ErrorMessage"]


# --- restJson1 ser/de ---
def serialize_json(value: ThrottledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ThrottledException_:
    out: ThrottledException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ThrottledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.xray#ThrottledException``."""

    code: str | None = "ThrottledException"

    def __init__(self, data: ThrottledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottledException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottledException":
        return cls(deserialize_json(data))
