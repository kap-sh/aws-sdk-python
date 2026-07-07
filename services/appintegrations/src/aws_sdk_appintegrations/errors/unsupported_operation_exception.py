"""Generated from Smithy shape ``com.amazonaws.appintegrations#UnsupportedOperationException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appintegrations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.message


class UnsupportedOperationException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appintegrations.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedOperationException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnsupportedOperationException_:
    out: UnsupportedOperationException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedOperationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appintegrations#UnsupportedOperationException``."""

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
    def from_json(cls, data: dict) -> "UnsupportedOperationException":
        return cls(deserialize_json(data))
