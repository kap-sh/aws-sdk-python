"""Generated from Smithy shape ``com.amazonaws.location#DescribeGeofenceCollectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_location.types.resource_name


class DescribeGeofenceCollectionRequest(TypedDict, closed=True):
    collection_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the geofence collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGeofenceCollectionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGeofenceCollectionRequest:
    out: DescribeGeofenceCollectionRequest = {}  # type: ignore[typeddict-item]
    return out
