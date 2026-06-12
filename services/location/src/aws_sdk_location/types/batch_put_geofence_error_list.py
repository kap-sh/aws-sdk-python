"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceErrorList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_location.types.batch_put_geofence_error

BatchPutGeofenceErrorList: TypeAlias = list["aws_sdk_location.types.batch_put_geofence_error.BatchPutGeofenceError"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceErrorList) -> list:
    import aws_sdk_location.types.batch_put_geofence_error
    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.batch_put_geofence_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchPutGeofenceErrorList:
    import aws_sdk_location.types.batch_put_geofence_error
    out: BatchPutGeofenceErrorList = []
    for item in data:
        out.append(aws_sdk_location.types.batch_put_geofence_error.deserialize_json(item))
    return out