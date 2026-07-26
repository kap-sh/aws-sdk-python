"""Generated from Smithy shape ``com.amazonaws.eks#ListInsightsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.insights_filter
    import capo_eks.types.list_insights_max_results
    import capo_eks.types.string


class ListInsightsRequest(TypedDict, closed=True):
    cluster_name: "capo_eks.types.string.String"
    """<p>The name of the Amazon EKS cluster associated with the insights.</p>"""
    filter: NotRequired["capo_eks.types.insights_filter.InsightsFilter"]
    """<p>The criteria to filter your list of insights for your cluster. You can filter which insights are returned by category, associated Kubernetes version, and status.</p>"""
    max_results: NotRequired[
        "capo_eks.types.list_insights_max_results.ListInsightsMaxResults"
    ]
    """<p>The maximum number of identity provider configurations returned by <code>ListInsights</code> in paginated output. When you use this parameter, <code>ListInsights</code> returns only <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListInsights</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If you don't use this parameter, <code>ListInsights</code> returns up to 100 results and a <code>nextToken</code> value, if applicable.</p>"""
    next_token: NotRequired["capo_eks.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListInsights</code> request. When the results of a <code>ListInsights</code> request exceed <code>maxResults</code>, you can use this value to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_eks.types.insights_filter

        out["filter"] = capo_eks.types.insights_filter.serialize_json(value["filter"])
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInsightsRequest:
    out: ListInsightsRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import capo_eks.types.insights_filter

        out["filter"] = capo_eks.types.insights_filter.deserialize_json(data["filter"])
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
