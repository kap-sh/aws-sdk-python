"""Generated from Smithy shape ``com.amazonaws.location#ListGeofenceCollectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.list_geofence_collections_response_entry_list
    import capo_location.types.token


class ListGeofenceCollectionsResponse(TypedDict, closed=True):
    entries: "capo_location.types.list_geofence_collections_response_entry_list.ListGeofenceCollectionsResponseEntryList"
    """<p>Lists the geofence collections that exist in your Amazon Web Services account.</p>"""
    next_token: NotRequired["capo_location.types.token.Token"]
    """<p>A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGeofenceCollectionsResponse) -> dict:
    out: dict = {}
    import capo_location.types.list_geofence_collections_response_entry_list

    out["Entries"] = (
        capo_location.types.list_geofence_collections_response_entry_list.serialize_json(
            value["entries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGeofenceCollectionsResponse:
    out: ListGeofenceCollectionsResponse = {}  # type: ignore[typeddict-item]
    if "Entries" in data:
        import capo_location.types.list_geofence_collections_response_entry_list

        out["entries"] = (
            capo_location.types.list_geofence_collections_response_entry_list.deserialize_json(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("ListGeofenceCollectionsResponse.entries required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
