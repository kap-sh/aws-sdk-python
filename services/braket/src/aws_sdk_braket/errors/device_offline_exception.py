"""Generated from Smithy shape ``com.amazonaws.braket#DeviceOfflineException``."""

from typing import TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import ServiceError


class DeviceOfflineException_(TypedDict):
    message: NotRequired["str"]


# --- restJson1 ser/de ---
def serialize_json(value: DeviceOfflineException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeviceOfflineException_:
    out: DeviceOfflineException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DeviceOfflineException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.braket#DeviceOfflineException``."""

    code: str | None = "DeviceOfflineException"

    def __init__(self, data: DeviceOfflineException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DeviceOfflineException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "DeviceOfflineException":
        return cls(deserialize_json(data))
