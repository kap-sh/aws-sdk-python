"""Generated from Smithy shape ``com.amazonaws.grafana#AccessDeniedException``."""

from typing import TypedDict
from aws_sdk_grafana.errors import DeserializationError
from aws_sdk_grafana.errors import ServiceError

class AccessDeniedException_(TypedDict):
    message: "str"

# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.grafana#AccessDeniedException``."""
    code: str | None = 'AccessDeniedException'

    def __init__(self, data: AccessDeniedException_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='AccessDeniedException')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_json(data))