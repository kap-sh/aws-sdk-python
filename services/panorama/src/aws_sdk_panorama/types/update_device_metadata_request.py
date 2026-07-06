"""Generated from Smithy shape ``com.amazonaws.panorama#UpdateDeviceMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.description
    import aws_sdk_panorama.types.device_id


class UpdateDeviceMetadataRequest(TypedDict, closed=True):
    device_id: "aws_sdk_panorama.types.device_id.DeviceId"
    """<p>The device's ID.</p>"""
    description: NotRequired["aws_sdk_panorama.types.description.Description"]
    """<p>A description for the device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeviceMetadataRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateDeviceMetadataRequest:
    out: UpdateDeviceMetadataRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
