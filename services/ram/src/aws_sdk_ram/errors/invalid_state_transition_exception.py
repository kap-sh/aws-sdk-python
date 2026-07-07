"""Generated from Smithy shape ``com.amazonaws.ram#InvalidStateTransitionException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ram.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_ram.types.string


class InvalidStateTransitionException_(TypedDict, closed=True):
    message: "aws_sdk_ram.types.string.String"


# --- restJson1 ser/de ---
def serialize_json(value: InvalidStateTransitionException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> InvalidStateTransitionException_:
    out: InvalidStateTransitionException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("InvalidStateTransitionException_.message required")
    return out


class InvalidStateTransitionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ram#InvalidStateTransitionException``."""

    code: str | None = "InvalidStateTransitionException"

    def __init__(self, data: InvalidStateTransitionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidStateTransitionException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidStateTransitionException":
        return cls(deserialize_json(data))
