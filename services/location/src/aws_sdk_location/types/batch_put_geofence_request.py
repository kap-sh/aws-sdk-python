"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_location.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_location.types.batch_put_geofence_request_entry_list
    import aws_sdk_location.types.resource_name

class BatchPutGeofenceRequest(TypedDict):
    collection_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The geofence collection storing the geofences.</p>"""
    entries: "aws_sdk_location.types.batch_put_geofence_request_entry_list.BatchPutGeofenceRequestEntryList"
    """<p>The batch of geofences to be stored in a geofence collection.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceRequest) -> dict:
    out: dict = {}
    import aws_sdk_location.types.batch_put_geofence_request_entry_list
    out["Entries"] = aws_sdk_location.types.batch_put_geofence_request_entry_list.serialize_json(value["entries"])
    return out


def deserialize_json(data: dict) -> BatchPutGeofenceRequest:
    out: BatchPutGeofenceRequest = {}  # type: ignore[typeddict-item]
    if "Entries" in data:
        import aws_sdk_location.types.batch_put_geofence_request_entry_list
        out["entries"] = aws_sdk_location.types.batch_put_geofence_request_entry_list.deserialize_json(data["Entries"])
    else:
        raise DeserializationError("BatchPutGeofenceRequest.entries required")
    return out