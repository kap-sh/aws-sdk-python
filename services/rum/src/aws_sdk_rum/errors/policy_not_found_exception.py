"""Generated from Smithy shape ``com.amazonaws.rum#PolicyNotFoundException``."""

from typing import TypedDict
from aws_sdk_rum.errors import DeserializationError
from aws_sdk_rum.errors import ServiceError

class PolicyNotFoundException_(TypedDict):
    message: "str"

# --- restJson1 ser/de ---
def serialize_json(value: PolicyNotFoundException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PolicyNotFoundException_:
    out: PolicyNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("PolicyNotFoundException_.message required")
    return out


class PolicyNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rum#PolicyNotFoundException``."""
    code: str | None = 'PolicyNotFoundException'

    def __init__(self, data: PolicyNotFoundException_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='PolicyNotFoundException')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PolicyNotFoundException":
        return cls(deserialize_json(data))