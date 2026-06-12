"""Generated from Smithy shape ``com.amazonaws.panorama#DeleteDeviceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_panorama.types.device_id


class DeleteDeviceResponse(TypedDict):
    device_id: NotRequired["aws_sdk_panorama.types.device_id.DeviceId"]
    """<p>The device's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeviceResponse) -> dict:
    out: dict = {}
    if "device_id" in value:
        out["DeviceId"] = value["device_id"]
    return out


def deserialize_json(data: dict) -> DeleteDeviceResponse:
    out: DeleteDeviceResponse = {}  # type: ignore[typeddict-item]
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    return out
