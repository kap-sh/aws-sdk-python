"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ListRecommendationSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cost_optimization_hub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.filter
    import aws_sdk_cost_optimization_hub.types.max_results
    import aws_sdk_cost_optimization_hub.types.summary_metrics_list


class ListRecommendationSummariesRequest(TypedDict, closed=True):
    filter: NotRequired["aws_sdk_cost_optimization_hub.types.filter.Filter"]
    group_by: "str"
    """<p>The grouping of recommendations by a dimension.</p>"""
    max_results: NotRequired[
        "aws_sdk_cost_optimization_hub.types.max_results.MaxResults"
    ]
    """<p>The maximum number of recommendations to be returned for the request.</p>"""
    metrics: NotRequired[
        "aws_sdk_cost_optimization_hub.types.summary_metrics_list.SummaryMetricsList"
    ]
    """<p>Additional metrics to be returned for the request. The only valid value is <code>savingsPercentage</code>.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to retrieve the next set of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendationSummariesRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_cost_optimization_hub.types.filter

        out["filter"] = (
            aws_sdk_cost_optimization_hub.types.filter.serialize_aws_json_1_0(
                value["filter"]
            )
        )
    out["groupBy"] = value["group_by"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "metrics" in value:
        import aws_sdk_cost_optimization_hub.types.summary_metrics_list

        out["metrics"] = (
            aws_sdk_cost_optimization_hub.types.summary_metrics_list.serialize_aws_json_1_0(
                value["metrics"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRecommendationSummariesRequest:
    out: ListRecommendationSummariesRequest = {}  # type: ignore[typeddict-item]
    if "filter" in data:
        import aws_sdk_cost_optimization_hub.types.filter

        out["filter"] = (
            aws_sdk_cost_optimization_hub.types.filter.deserialize_aws_json_1_0(
                data["filter"]
            )
        )
    if "groupBy" in data:
        out["group_by"] = data["groupBy"]
    else:
        raise DeserializationError(
            "ListRecommendationSummariesRequest.group_by required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "metrics" in data:
        import aws_sdk_cost_optimization_hub.types.summary_metrics_list

        out["metrics"] = (
            aws_sdk_cost_optimization_hub.types.summary_metrics_list.deserialize_aws_json_1_0(
                data["metrics"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
