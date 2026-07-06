"""Generated from Smithy shape ``com.amazonaws.personalize#ListDatasetGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.max_results
    import aws_sdk_personalize.types.next_token


class ListDatasetGroupsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_personalize.types.next_token.NextToken"]
    """<p>A token returned from the previous call to <code>ListDatasetGroups</code> for getting the next set of dataset groups (if they exist).</p>"""
    max_results: NotRequired["aws_sdk_personalize.types.max_results.MaxResults"]
    """<p>The maximum number of dataset groups to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDatasetGroupsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDatasetGroupsRequest:
    out: ListDatasetGroupsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
