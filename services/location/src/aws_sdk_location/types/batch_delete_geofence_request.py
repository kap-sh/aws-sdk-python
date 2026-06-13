"""Generated from Smithy shape ``com.amazonaws.location#BatchDeleteGeofenceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_location.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_location.types.id_list
    import aws_sdk_location.types.resource_name


class BatchDeleteGeofenceRequest(TypedDict):
    collection_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The geofence collection storing the geofences to be deleted.</p>"""
    geofence_ids: "aws_sdk_location.types.id_list.IdList"
    """<p>The batch of geofences to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteGeofenceRequest) -> dict:
    out: dict = {}
    import aws_sdk_location.types.id_list

    out["GeofenceIds"] = aws_sdk_location.types.id_list.serialize_json(
        value["geofence_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteGeofenceRequest:
    out: BatchDeleteGeofenceRequest = {}  # type: ignore[typeddict-item]
    if "GeofenceIds" in data:
        import aws_sdk_location.types.id_list

        out["geofence_ids"] = aws_sdk_location.types.id_list.deserialize_json(
            data["GeofenceIds"]
        )
    else:
        raise DeserializationError("BatchDeleteGeofenceRequest.geofence_ids required")
    return out
