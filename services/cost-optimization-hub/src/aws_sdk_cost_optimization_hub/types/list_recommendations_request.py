"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ListRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.filter
    import aws_sdk_cost_optimization_hub.types.max_results
    import aws_sdk_cost_optimization_hub.types.order_by


class ListRecommendationsRequest(TypedDict, closed=True):
    filter: NotRequired["aws_sdk_cost_optimization_hub.types.filter.Filter"]
    """<p>The constraints that you want all returned recommendations to match.</p>"""
    order_by: NotRequired["aws_sdk_cost_optimization_hub.types.order_by.OrderBy"]
    """<p>The ordering of recommendations by a dimension.</p>"""
    include_all_recommendations: "bool"
    """<p>List of all recommendations for a resource, or a single recommendation if de-duped by <code>resourceId</code>.</p>"""
    max_results: NotRequired[
        "aws_sdk_cost_optimization_hub.types.max_results.MaxResults"
    ]
    """<p>The maximum number of recommendations that are returned for the request.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendationsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_cost_optimization_hub.types.filter

        out["filter"] = (
            aws_sdk_cost_optimization_hub.types.filter.serialize_aws_json_1_0(
                value["filter"]
            )
        )
    if "order_by" in value:
        import aws_sdk_cost_optimization_hub.types.order_by

        out["orderBy"] = (
            aws_sdk_cost_optimization_hub.types.order_by.serialize_aws_json_1_0(
                value["order_by"]
            )
        )
    out["includeAllRecommendations"] = value.get("include_all_recommendations", False)
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRecommendationsRequest:
    out: ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_cost_optimization_hub.types.filter

        out["filter"] = (
            aws_sdk_cost_optimization_hub.types.filter.deserialize_aws_json_1_0(
                data["filter"]
            )
        )
    if "orderBy" in data:
        import aws_sdk_cost_optimization_hub.types.order_by

        out["order_by"] = (
            aws_sdk_cost_optimization_hub.types.order_by.deserialize_aws_json_1_0(
                data["orderBy"]
            )
        )
    if "includeAllRecommendations" in data:
        out["include_all_recommendations"] = data["includeAllRecommendations"]
    else:
        out["include_all_recommendations"] = False
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
