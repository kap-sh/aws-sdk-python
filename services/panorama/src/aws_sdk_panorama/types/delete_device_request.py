"""Generated from Smithy shape ``com.amazonaws.panorama#DeleteDeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.device_id


class DeleteDeviceRequest(TypedDict):
    device_id: "aws_sdk_panorama.types.device_id.DeviceId"
    """<p>The device's ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDeviceRequest:
    out: DeleteDeviceRequest = {}  # type: ignore[typeddict-item]
    return out
