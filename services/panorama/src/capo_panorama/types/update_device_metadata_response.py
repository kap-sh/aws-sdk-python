"""Generated from Smithy shape ``com.amazonaws.panorama#UpdateDeviceMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.device_id


class UpdateDeviceMetadataResponse(TypedDict, closed=True):
    device_id: NotRequired["capo_panorama.types.device_id.DeviceId"]
    """<p>The device's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeviceMetadataResponse) -> dict:
    out: dict = {}
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    return out


def deserialize_json(data: dict) -> UpdateDeviceMetadataResponse:
    out: UpdateDeviceMetadataResponse = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    return out
