"""Generated from Smithy shape ``com.amazonaws.scheduler#ConflictException``."""

from typing_extensions import TypedDict

from capo_scheduler.errors import DeserializationError, ServiceError


class ConflictException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.scheduler#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict, message: str | None = None) -> "ConflictException":
        return cls(deserialize_json(data), message)
