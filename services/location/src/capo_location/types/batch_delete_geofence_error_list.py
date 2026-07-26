"""Generated from Smithy shape ``com.amazonaws.location#BatchDeleteGeofenceErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_location.types.batch_delete_geofence_error

BatchDeleteGeofenceErrorList: TypeAlias = list[
    "capo_location.types.batch_delete_geofence_error.BatchDeleteGeofenceError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteGeofenceErrorList) -> list:
    import capo_location.types.batch_delete_geofence_error

    out: list = []
    for item in value:
        out.append(capo_location.types.batch_delete_geofence_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchDeleteGeofenceErrorList:
    import capo_location.types.batch_delete_geofence_error

    out: BatchDeleteGeofenceErrorList = []
    for item in data:
        out.append(
            capo_location.types.batch_delete_geofence_error.deserialize_json(item)
        )
    return out
