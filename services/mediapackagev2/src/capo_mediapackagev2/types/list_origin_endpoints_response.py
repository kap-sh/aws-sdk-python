"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListOriginEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.origin_endpoints_list


class ListOriginEndpointsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mediapackagev2.types.origin_endpoints_list.OriginEndpointsList"
    ]
    """<p>The objects being returned.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token from the GET list request. Use the token to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOriginEndpointsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mediapackagev2.types.origin_endpoints_list

        out["Items"] = capo_mediapackagev2.types.origin_endpoints_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOriginEndpointsResponse:
    out: ListOriginEndpointsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_mediapackagev2.types.origin_endpoints_list

        out["items"] = capo_mediapackagev2.types.origin_endpoints_list.deserialize_json(
            data["Items"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
