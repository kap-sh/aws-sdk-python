"""Generated from Smithy shape ``com.amazonaws.location#DeleteGeofenceCollectionRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_location.types.resource_name

class DeleteGeofenceCollectionRequest(TypedDict):
    collection_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the geofence collection to be deleted.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteGeofenceCollectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGeofenceCollectionRequest:
    out: DeleteGeofenceCollectionRequest = {}  # type: ignore[typeddict-item]
    return out