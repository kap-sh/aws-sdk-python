"""Generated from Smithy shape ``com.amazonaws.location#GetGeofenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.id
    import capo_location.types.resource_name


class GetGeofenceRequest(TypedDict, closed=True):
    collection_name: "capo_location.types.resource_name.ResourceName"
    """<p>The geofence collection storing the target geofence.</p>"""
    geofence_id: "capo_location.types.id.Id"
    """<p>The geofence you're retrieving details for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGeofenceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGeofenceRequest:
    out: GetGeofenceRequest = {}  # type: ignore[typeddict-item]
    return out
