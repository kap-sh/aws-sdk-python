"""Generated from Smithy shape ``com.amazonaws.location#GetGeofenceRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_location.types.id
    import aws_sdk_location.types.resource_name

class GetGeofenceRequest(TypedDict):
    collection_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The geofence collection storing the target geofence.</p>"""
    geofence_id: "aws_sdk_location.types.id.Id"
    """<p>The geofence you're retrieving details for.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetGeofenceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGeofenceRequest:
    out: GetGeofenceRequest = {}  # type: ignore[typeddict-item]
    return out