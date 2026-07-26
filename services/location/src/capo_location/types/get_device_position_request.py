"""Generated from Smithy shape ``com.amazonaws.location#GetDevicePositionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.id
    import capo_location.types.resource_name


class GetDevicePositionRequest(TypedDict, closed=True):
    tracker_name: "capo_location.types.resource_name.ResourceName"
    """<p>The tracker resource receiving the position update.</p>"""
    device_id: "capo_location.types.id.Id"
    """<p>The device whose position you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDevicePositionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDevicePositionRequest:
    out: GetDevicePositionRequest = {}  # type: ignore[typeddict-item]
    return out
