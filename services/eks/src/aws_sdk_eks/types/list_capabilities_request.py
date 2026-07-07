"""Generated from Smithy shape ``com.amazonaws.eks#ListCapabilitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.list_capabilities_request_max_results
    import aws_sdk_eks.types.string


class ListCapabilitiesRequest(TypedDict, closed=True):
    cluster_name: "aws_sdk_eks.types.string.String"
    """<p>The name of the Amazon EKS cluster for which you want to list capabilities.</p>"""
    next_token: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p>"""
    max_results: NotRequired[
        "aws_sdk_eks.types.list_capabilities_request_max_results.ListCapabilitiesRequestMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value. If you don't specify a value, the default is 100 results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCapabilitiesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCapabilitiesRequest:
    out: ListCapabilitiesRequest = {}  # type: ignore[typeddict-item]
    return out
