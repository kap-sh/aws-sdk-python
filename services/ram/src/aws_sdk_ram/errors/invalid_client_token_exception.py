"""Generated from Smithy shape ``com.amazonaws.ram#InvalidClientTokenException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class InvalidClientTokenException_(TypedDict, closed=True):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidClientTokenException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidClientTokenException_:
    out: InvalidClientTokenException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidClientTokenException_.message required")
    return out


class InvalidClientTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#InvalidClientTokenException``."""

    code: str | None = "InvalidClientTokenException"

    def __init__(self, data: InvalidClientTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidClientTokenException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidClientTokenException":
        return cls(deserialize_json(data))
