"""Generated from Smithy shape ``com.amazonaws.braket#DeviceRetiredException``."""

from typing import TypedDict
from typing_extensions import NotRequired
from aws_sdk_braket.errors import ServiceError

class DeviceRetiredException_(TypedDict):
    message: NotRequired["str"]

# --- restJson1 ser/de ---
def serialize_json(value: DeviceRetiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeviceRetiredException_:
    out: DeviceRetiredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DeviceRetiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.braket#DeviceRetiredException``."""
    code: str | None = 'DeviceRetiredException'

    def __init__(self, data: DeviceRetiredException_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='DeviceRetiredException')
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DeviceRetiredException":
        return cls(deserialize_json(data))