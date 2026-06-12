"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetDeviceProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.device_profile_id


class GetDeviceProfileRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.device_profile_id.DeviceProfileId"
    """<p>The ID of the resource to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeviceProfileRequest:
    out: GetDeviceProfileRequest = {}  # type: ignore[typeddict-item]
    return out
