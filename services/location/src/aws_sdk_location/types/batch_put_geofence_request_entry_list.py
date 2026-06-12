"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_location.types.batch_put_geofence_request_entry

BatchPutGeofenceRequestEntryList: TypeAlias = list["aws_sdk_location.types.batch_put_geofence_request_entry.BatchPutGeofenceRequestEntry"]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceRequestEntryList) -> list:
    import aws_sdk_location.types.batch_put_geofence_request_entry
    out: list = []
    for item in value:
        out.append(aws_sdk_location.types.batch_put_geofence_request_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchPutGeofenceRequestEntryList:
    import aws_sdk_location.types.batch_put_geofence_request_entry
    out: BatchPutGeofenceRequestEntryList = []
    for item in data:
        out.append(aws_sdk_location.types.batch_put_geofence_request_entry.deserialize_json(item))
    return out