"""Generated from Smithy shape ``com.amazonaws.eks#ListUpdatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.list_updates_request_max_results
    import aws_sdk_eks.types.string


class ListUpdatesRequest(TypedDict):
    name: "aws_sdk_eks.types.string.String"
    """<p>The name of the Amazon EKS cluster to list updates for.</p>"""
    nodegroup_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the Amazon EKS managed node group to list updates for.</p>"""
    addon_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The names of the installed add-ons that have available updates.</p>"""
    capability_name: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The name of the capability for which you want to list updates.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired[
        "aws_sdk_eks.types.list_updates_request_max_results.ListUpdatesRequestMaxResults"
    ]
    """<p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUpdatesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListUpdatesRequest:
    out: ListUpdatesRequest = {}  # type: ignore[typeddict-item]
    return out
