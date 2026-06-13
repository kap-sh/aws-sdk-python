"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.batch_item_error
    import aws_sdk_location.types.id


class BatchPutGeofenceError(TypedDict):
    geofence_id: "aws_sdk_location.types.id.Id"
    """<p>The geofence associated with the error message.</p>"""
    error: "aws_sdk_location.types.batch_item_error.BatchItemError"
    """<p>Contains details associated to the batch error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceError) -> dict:
    out: dict = {}
    out["GeofenceId"] = value["geofence_id"]
    import aws_sdk_location.types.batch_item_error

    out["Error"] = aws_sdk_location.types.batch_item_error.serialize_json(
        value["error"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutGeofenceError:
    out: BatchPutGeofenceError = {}  # type: ignore[typeddict-item]
    if "GeofenceId" in data:
        out["geofence_id"] = data["GeofenceId"]
    else:
        raise DeserializationError("BatchPutGeofenceError.geofence_id required")
    if "Error" in data:
        import aws_sdk_location.types.batch_item_error

        out["error"] = aws_sdk_location.types.batch_item_error.deserialize_json(
            data["Error"]
        )
    else:
        raise DeserializationError("BatchPutGeofenceError.error required")
    return out
