"""Generated from Smithy shape ``com.amazonaws.location#DescribeGeofenceCollectionRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_location.types.resource_name

class DescribeGeofenceCollectionRequest(TypedDict):
    collection_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the geofence collection.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeGeofenceCollectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGeofenceCollectionRequest:
    out: DescribeGeofenceCollectionRequest = {}  # type: ignore[typeddict-item]
    return out