"""Generated from Smithy shape ``com.amazonaws.eks#ListFargateProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.fargate_profiles_request_max_results
    import capo_eks.types.string


class ListFargateProfilesRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of your cluster.</p>"""
    max_results: NotRequired[
        "capo_eks.types.fargate_profiles_request_max_results.FargateProfilesRequestMaxResults"
    ]
    """<p>The maximum number of results, returned in paginated output. You receive <code>maxResults</code> in a single page, along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, 100 results and a <code>nextToken</code> value, if applicable, are returned.</p>"""
    next_token: NotRequired["capo_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request, where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is null when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is used only to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFargateProfilesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFargateProfilesRequest:
    out: ListFargateProfilesRequest = {}  # type: ignore[typeddict-item]
    return out
