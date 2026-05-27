"""Generated from Smithy shape ``com.amazonaws.eks#ListAccessEntriesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.list_access_entries_request_max_results
    import aws_sdk_eks.types.string


class ListAccessEntriesRequest(TypedDict):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    associated_policy_arn: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The ARN of an <code>AccessPolicy</code>. When you specify an access policy ARN, only the access entries associated to that access policy are returned. For a list of available policy ARNs, use <code>ListAccessPolicies</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_eks.types.list_access_entries_request_max_results.ListAccessEntriesRequestMaxResults"
    ]
    """<p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccessEntriesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAccessEntriesRequest:
    out: ListAccessEntriesRequest = {}  # type: ignore[typeddict-item]
    return out
