"""Generated from Smithy shape ``com.amazonaws.location#ListTrackerConsumersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_location.types.resource_name
    import aws_sdk_location.types.token


class ListTrackerConsumersRequest(TypedDict):
    tracker_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The tracker resource whose associated geofence collections you want to list.</p>"""
    max_results: NotRequired["int"]
    """<p>An optional limit for the number of resources returned in a single call. </p> <p>Default value: <code>100</code> </p>"""
    next_token: NotRequired["aws_sdk_location.types.token.Token"]
    """<p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page. </p> <p>Default value: <code>null</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrackerConsumersRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTrackerConsumersRequest:
    out: ListTrackerConsumersRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
