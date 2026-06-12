"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#GetDeviceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.device_id


class GetDeviceRequest(TypedDict):
    id: "aws_sdk_workspaces_thin_client.types.device_id.DeviceId"
    """<p>The ID of the device for which to return information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDeviceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDeviceRequest:
    out: GetDeviceRequest = {}  # type: ignore[typeddict-item]
    return out
