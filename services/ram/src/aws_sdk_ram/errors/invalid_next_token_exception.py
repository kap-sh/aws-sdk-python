"""Generated from Smithy shape ``com.amazonaws.ram#InvalidNextTokenException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class InvalidNextTokenException_(TypedDict, closed=True):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidNextTokenException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidNextTokenException_:
    out: InvalidNextTokenException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidNextTokenException_.message required")
    return out


class InvalidNextTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#InvalidNextTokenException``."""

    code: str | None = "InvalidNextTokenException"

    def __init__(self, data: InvalidNextTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidNextTokenException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidNextTokenException":
        return cls(deserialize_json(data))
