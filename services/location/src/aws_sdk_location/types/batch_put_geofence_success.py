"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceSuccess``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_location.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_location.types.id
    import aws_sdk_location.types.timestamp

class BatchPutGeofenceSuccess(TypedDict):
    geofence_id: "aws_sdk_location.types.id.Id"
    """<p>The geofence successfully stored in a geofence collection.</p>"""
    create_time: "aws_sdk_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the geofence was stored in a geofence collection in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    update_time: "aws_sdk_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the geofence was last updated in <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceSuccess) -> dict:
    out: dict = {}
    out["GeofenceId"] = value["geofence_id"]
    import aws_sdk_location.types.timestamp
    out["CreateTime"] = aws_sdk_location.types.timestamp.serialize_json(value["create_time"])
    import aws_sdk_location.types.timestamp
    out["UpdateTime"] = aws_sdk_location.types.timestamp.serialize_json(value["update_time"])
    return out


def deserialize_json(data: dict) -> BatchPutGeofenceSuccess:
    out: BatchPutGeofenceSuccess = {}  # type: ignore[typeddict-item]
    if "GeofenceId" in data:
        out["geofence_id"] = data["GeofenceId"]
    else:
        raise DeserializationError("BatchPutGeofenceSuccess.geofence_id required")
    if "CreateTime" in data:
        import aws_sdk_location.types.timestamp
        out["create_time"] = aws_sdk_location.types.timestamp.deserialize_json(data["CreateTime"])
    else:
        raise DeserializationError("BatchPutGeofenceSuccess.create_time required")
    if "UpdateTime" in data:
        import aws_sdk_location.types.timestamp
        out["update_time"] = aws_sdk_location.types.timestamp.deserialize_json(data["UpdateTime"])
    else:
        raise DeserializationError("BatchPutGeofenceSuccess.update_time required")
    return out