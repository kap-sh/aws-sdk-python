"""Generated from Smithy shape ``com.amazonaws.pcs#ListComputeNodeGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_pcs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pcs.types.cluster_identifier
    import aws_sdk_pcs.types.max_results


class ListComputeNodeGroupsRequest(TypedDict, closed=True):
    cluster_identifier: "aws_sdk_pcs.types.cluster_identifier.ClusterIdentifier"
    """<p>The name or ID of the cluster to list compute node groups for.</p>"""
    next_token: NotRequired["str"]
    """<p>The value of <code>nextToken</code> is a unique pagination token for each page of results returned. If <code>nextToken</code> is returned, there are more results available. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token returns an <code>HTTP 400 InvalidToken</code> error.</p>"""
    max_results: "aws_sdk_pcs.types.max_results.MaxResults"
    """<p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results. The default is 10 results, and the maximum allowed page size is 100 results. A value of 0 uses the default.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListComputeNodeGroupsRequest) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["maxResults"] = value.get("max_results", 10)
    return out


def deserialize_aws_json_1_0(data: dict) -> ListComputeNodeGroupsRequest:
    out: ListComputeNodeGroupsRequest = {}  # type: ignore[typeddict-item]
    if "clusterIdentifier" in data:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        raise DeserializationError(
            "ListComputeNodeGroupsRequest.cluster_identifier required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 10
    return out
