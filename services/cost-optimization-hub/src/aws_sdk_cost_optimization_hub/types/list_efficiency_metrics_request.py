"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ListEfficiencyMetricsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cost_optimization_hub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.granularity_type
    import aws_sdk_cost_optimization_hub.types.max_results
    import aws_sdk_cost_optimization_hub.types.order_by
    import aws_sdk_cost_optimization_hub.types.time_period


class ListEfficiencyMetricsRequest(TypedDict, closed=True):
    group_by: NotRequired["str"]
    """<p>The dimension by which to group the cost efficiency metrics. Valid values include account ID, Amazon Web Services Region. When no grouping is specified, metrics are aggregated across all resources in the specified time period.</p>"""
    granularity: "aws_sdk_cost_optimization_hub.types.granularity_type.GranularityType"
    """<p>The time granularity for the cost efficiency metrics. Specify <code>Daily</code> for metrics aggregated by day, or <code>Monthly</code> for metrics aggregated by month.</p>"""
    time_period: "aws_sdk_cost_optimization_hub.types.time_period.TimePeriod"
    """<p>The time period for which to retrieve the cost efficiency metrics. The start date is inclusive and the end date is exclusive. Dates can be specified in either YYYY-MM-DD format or YYYY-MM format depending on the desired granularity.</p>"""
    max_results: NotRequired[
        "aws_sdk_cost_optimization_hub.types.max_results.MaxResults"
    ]
    """<p>The maximum number of groups to return in the response. Valid values range from 0 to 1000. Use in conjunction with <code>nextToken</code> to paginate through results when the total number of groups exceeds this limit.</p>"""
    order_by: NotRequired["aws_sdk_cost_optimization_hub.types.order_by.OrderBy"]
    """<p>The ordering specification for the results. Defines which dimension to sort by and whether to sort in ascending or descending order.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to retrieve the next page of results. This value is returned in the response when the number of groups exceeds the specified <code>maxResults</code> value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEfficiencyMetricsRequest) -> dict:
    out: dict = {}
    if "group_by" in value:
        out["groupBy"] = value["group_by"]
    import aws_sdk_cost_optimization_hub.types.granularity_type

    out["granularity"] = (
        aws_sdk_cost_optimization_hub.types.granularity_type.serialize_aws_json_1_0(
            value["granularity"]
        )
    )
    import aws_sdk_cost_optimization_hub.types.time_period

    out["timePeriod"] = (
        aws_sdk_cost_optimization_hub.types.time_period.serialize_aws_json_1_0(
            value["time_period"]
        )
    )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "order_by" in value:
        import aws_sdk_cost_optimization_hub.types.order_by

        out["orderBy"] = (
            aws_sdk_cost_optimization_hub.types.order_by.serialize_aws_json_1_0(
                value["order_by"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEfficiencyMetricsRequest:
    out: ListEfficiencyMetricsRequest = {}  # type: ignore[typeddict-item]
    if "groupBy" in data:
        out["group_by"] = data["groupBy"]
    if "granularity" in data:
        import aws_sdk_cost_optimization_hub.types.granularity_type

        out["granularity"] = (
            aws_sdk_cost_optimization_hub.types.granularity_type.deserialize_aws_json_1_0(
                data["granularity"]
            )
        )
    else:
        raise DeserializationError("ListEfficiencyMetricsRequest.granularity required")
    if "timePeriod" in data:
        import aws_sdk_cost_optimization_hub.types.time_period

        out["time_period"] = (
            aws_sdk_cost_optimization_hub.types.time_period.deserialize_aws_json_1_0(
                data["timePeriod"]
            )
        )
    else:
        raise DeserializationError("ListEfficiencyMetricsRequest.time_period required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "orderBy" in data:
        import aws_sdk_cost_optimization_hub.types.order_by

        out["order_by"] = (
            aws_sdk_cost_optimization_hub.types.order_by.deserialize_aws_json_1_0(
                data["orderBy"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
