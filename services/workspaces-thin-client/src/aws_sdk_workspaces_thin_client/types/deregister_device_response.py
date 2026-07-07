"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#DeregisterDeviceResponse``."""

from typing_extensions import TypedDict


class DeregisterDeviceResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterDeviceResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterDeviceResponse:
    out: DeregisterDeviceResponse = {}  # type: ignore[typeddict-item]
    return out
