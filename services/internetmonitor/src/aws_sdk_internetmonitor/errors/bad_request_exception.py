"""Generated from Smithy shape ``com.amazonaws.internetmonitor#BadRequestException``."""

from typing import TypedDict
from typing_extensions import NotRequired
from aws_sdk_internetmonitor.errors import ServiceError

class BadRequestException_(TypedDict):
    message: NotRequired["str"]

# --- restJson1 ser/de ---
def serialize_json(value: BadRequestException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BadRequestException_:
    out: BadRequestException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class BadRequestException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.internetmonitor#BadRequestException``."""
    code: str | None = 'BadRequestException'

    def __init__(self, data: BadRequestException_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='BadRequestException')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BadRequestException":
        return cls(deserialize_json(data))