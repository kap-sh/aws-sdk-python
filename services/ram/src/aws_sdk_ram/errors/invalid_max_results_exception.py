"""Generated from Smithy shape ``com.amazonaws.ram#InvalidMaxResultsException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class InvalidMaxResultsException_(TypedDict, closed=True):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidMaxResultsException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidMaxResultsException_:
    out: InvalidMaxResultsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidMaxResultsException_.message required")
    return out


class InvalidMaxResultsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#InvalidMaxResultsException``."""

    code: str | None = "InvalidMaxResultsException"

    def __init__(self, data: InvalidMaxResultsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidMaxResultsException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidMaxResultsException":
        return cls(deserialize_json(data))
