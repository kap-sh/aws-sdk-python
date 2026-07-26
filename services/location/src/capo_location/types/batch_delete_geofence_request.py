"""Generated from Smithy shape ``com.amazonaws.location#BatchDeleteGeofenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.id_list
    import capo_location.types.resource_name


class BatchDeleteGeofenceRequest(TypedDict, closed=True):
    collection_name: "capo_location.types.resource_name.ResourceName"
    """<p>The geofence collection storing the geofences to be deleted.</p>"""
    geofence_ids: "capo_location.types.id_list.IdList"
    """<p>The batch of geofences to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteGeofenceRequest) -> dict:
    out: dict = {}
    import capo_location.types.id_list

    out["GeofenceIds"] = capo_location.types.id_list.serialize_json(
        value["geofence_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteGeofenceRequest:
    out: BatchDeleteGeofenceRequest = {}  # type: ignore[typeddict-item]
    if "GeofenceIds" in data:
        import capo_location.types.id_list

        out["geofence_ids"] = capo_location.types.id_list.deserialize_json(
            data["GeofenceIds"]
        )
    else:
        raise DeserializationError("BatchDeleteGeofenceRequest.geofence_ids required")
    return out
