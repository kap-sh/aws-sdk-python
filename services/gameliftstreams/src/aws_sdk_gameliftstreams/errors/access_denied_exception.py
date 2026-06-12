"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#AccessDeniedException``."""

from typing import TypedDict
from aws_sdk_gameliftstreams.errors import DeserializationError
from aws_sdk_gameliftstreams.errors import ServiceError

class AccessDeniedException_(TypedDict):
    message: "str"
    """<p>Description of the error.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AccessDeniedException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("AccessDeniedException_.message required")
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.gameliftstreams#AccessDeniedException``."""
    code: str | None = 'AccessDeniedException'

    def __init__(self, data: AccessDeniedException_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='AccessDeniedException')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_json(data))