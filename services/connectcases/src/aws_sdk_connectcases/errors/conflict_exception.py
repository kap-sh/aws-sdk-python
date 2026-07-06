"""Generated from Smithy shape ``com.amazonaws.connectcases#ConflictException``."""

from typing_extensions import TypedDict

from aws_sdk_connectcases.errors import DeserializationError, ServiceError


class ConflictException_(TypedDict, closed=True):
    message: "str"


# --- restJson1 ser/de ---
def serialize_json(value: ConflictException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ConflictException_.message required")
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connectcases#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(self, data: ConflictException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ConflictException":
        return cls(deserialize_json(data))
