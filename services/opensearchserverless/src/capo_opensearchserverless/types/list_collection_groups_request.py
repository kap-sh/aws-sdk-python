"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#ListCollectionGroupsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListCollectionGroupsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>If your initial <code>ListCollectionGroups</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListCollectionGroups</code> operations, which returns results in the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return. Default is 20. You can use <code>nextToken</code> to get the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCollectionGroupsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCollectionGroupsRequest:
    out: ListCollectionGroupsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
