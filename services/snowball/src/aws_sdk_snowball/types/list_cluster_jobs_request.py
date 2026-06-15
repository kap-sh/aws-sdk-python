"""Generated from Smithy shape ``com.amazonaws.snowball#ListClusterJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.cluster_id
    import aws_sdk_snowball.types.list_limit
    import aws_sdk_snowball.types.string


class ListClusterJobsRequest(TypedDict):
    cluster_id: "aws_sdk_snowball.types.cluster_id.ClusterId"
    """<p>The 39-character ID for the cluster that you want to list, for example <code>CID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""
    max_results: NotRequired["aws_sdk_snowball.types.list_limit.ListLimit"]
    """<p>The number of <code>JobListEntry</code> objects to return.</p>"""
    next_token: NotRequired["aws_sdk_snowball.types.string.String"]
    r"""<p>HTTP requests are stateless. To identify what object comes \"next\" in the list of <code>JobListEntry</code> objects, you have the option of specifying <code>NextToken</code> as the starting point for your returned list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterJobsRequest) -> dict:
    out: dict = {}
    out["ClusterId"] = value["cluster_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterJobsRequest:
    out: ListClusterJobsRequest = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    else:
        raise DeserializationError("ListClusterJobsRequest.cluster_id required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
