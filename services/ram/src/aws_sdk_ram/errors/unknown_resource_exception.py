"""Generated from Smithy shape ``com.amazonaws.ram#UnknownResourceException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class UnknownResourceException_(TypedDict, closed=True):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: UnknownResourceException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnknownResourceException_:
    out: UnknownResourceException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("UnknownResourceException_.message required")
    return out


class UnknownResourceException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#UnknownResourceException``."""

    code: str | None = "UnknownResourceException"

    def __init__(self, data: UnknownResourceException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnknownResourceException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "UnknownResourceException":
        return cls(deserialize_json(data))
