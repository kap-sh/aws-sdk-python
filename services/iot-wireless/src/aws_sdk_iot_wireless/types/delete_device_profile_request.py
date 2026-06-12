"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteDeviceProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.device_profile_id


class DeleteDeviceProfileRequest(TypedDict):
    id: "aws_sdk_iot_wireless.types.device_profile_id.DeviceProfileId"
    """<p>The ID of the resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeviceProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDeviceProfileRequest:
    out: DeleteDeviceProfileRequest = {}  # type: ignore[typeddict-item]
    return out
