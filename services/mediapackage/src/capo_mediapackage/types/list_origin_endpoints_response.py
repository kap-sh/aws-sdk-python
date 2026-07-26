"""Generated from Smithy shape ``com.amazonaws.mediapackage#ListOriginEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__list_of_origin_endpoint
    import capo_mediapackage.types.__string


class ListOriginEndpointsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_mediapackage.types.__string.__string"]
    """A token that can be used to resume pagination from the end of the collection."""
    origin_endpoints: NotRequired[
        "capo_mediapackage.types.__list_of_origin_endpoint.__listOfOriginEndpoint"
    ]
    """A list of OriginEndpoint records."""


# --- restJson1 ser/de ---
def serialize_json(value: ListOriginEndpointsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "origin_endpoints" in value:
        import capo_mediapackage.types.__list_of_origin_endpoint

        out["originEndpoints"] = (
            capo_mediapackage.types.__list_of_origin_endpoint.serialize_json(
                value["origin_endpoints"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListOriginEndpointsResponse:
    out: ListOriginEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "originEndpoints" in data:
        import capo_mediapackage.types.__list_of_origin_endpoint

        out["origin_endpoints"] = (
            capo_mediapackage.types.__list_of_origin_endpoint.deserialize_json(
                data["originEndpoints"]
            )
        )
    return out
