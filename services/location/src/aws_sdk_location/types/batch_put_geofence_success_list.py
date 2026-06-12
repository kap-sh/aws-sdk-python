"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceSuccessList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_location.types.batch_put_geofence_success

BatchPutGeofenceSuccessList: TypeAlias = list["aws_sdk_location.types.batch_put_geofence_success.BatchPutGeofenceSuccess"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceSuccessList) -> list:
    import aws_sdk_location.types.batch_put_geofence_success
    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.batch_put_geofence_success.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchPutGeofenceSuccessList:
    import aws_sdk_location.types.batch_put_geofence_success
    out: BatchPutGeofenceSuccessList = []
    for item in data:
        out.append(aws_sdk_location.types.batch_put_geofence_success.deserialize_json(item))
    return out