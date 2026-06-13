"""Generated from Smithy shape ``com.amazonaws.location#GetDevicePositionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.id
    import aws_sdk_location.types.resource_name


class GetDevicePositionRequest(TypedDict):
    tracker_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The tracker resource receiving the position update.</p>"""
    device_id: "aws_sdk_location.types.id.Id"
    """<p>The device whose position you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDevicePositionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDevicePositionRequest:
    out: GetDevicePositionRequest = {}  # type: ignore[typeddict-item]
    return out
