"""Generated from Smithy shape ``com.amazonaws.location#ListGeofencesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_location.types.large_token
    import aws_sdk_location.types.resource_name


class ListGeofencesRequest(TypedDict):
    collection_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the geofence collection storing the list of geofences.</p>"""
    next_token: NotRequired["aws_sdk_location.types.large_token.LargeToken"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p> <p>Default value: <code>null</code> </p>"""
    max_results: NotRequired["int"]
    """<p>An optional limit for the number of geofences returned in a single call. </p> <p>Default value: <code>100</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGeofencesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListGeofencesRequest:
    out: ListGeofencesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
