"""Generated from Smithy shape ``com.amazonaws.location#ListGeofenceCollectionsResponseEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.list_geofence_collections_response_entry

ListGeofenceCollectionsResponseEntryList: TypeAlias = list[
    "aws_sdk_location.types.list_geofence_collections_response_entry.ListGeofenceCollectionsResponseEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListGeofenceCollectionsResponseEntryList) -> list:
    import aws_sdk_location.types.list_geofence_collections_response_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_location.types.list_geofence_collections_response_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListGeofenceCollectionsResponseEntryList:
    import aws_sdk_location.types.list_geofence_collections_response_entry

    out: ListGeofenceCollectionsResponseEntryList = []
    for item in data:
        out.append(
            aws_sdk_location.types.list_geofence_collections_response_entry.deserialize_json(
                item
            )
        )
    return out
