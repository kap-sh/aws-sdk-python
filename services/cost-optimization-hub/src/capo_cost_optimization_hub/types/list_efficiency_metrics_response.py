"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ListEfficiencyMetricsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.efficiency_metrics_by_group_list


class ListEfficiencyMetricsResponse(TypedDict, closed=True):
    efficiency_metrics_by_group: NotRequired[
        "capo_cost_optimization_hub.types.efficiency_metrics_by_group_list.EfficiencyMetricsByGroupList"
    ]
    """<p>A list of cost efficiency metrics grouped by the specified dimension. Each group contains time-series data points with cost efficiency, potential savings, and optimzable spend for the specified time period.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to retrieve the next page of results. When this value is present in the response, additional groups are available. Pass this token in the <code>nextToken</code> parameter of a subsequent request to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEfficiencyMetricsResponse) -> dict:
    out: dict = {}
    if "efficiency_metrics_by_group" in value:
        import capo_cost_optimization_hub.types.efficiency_metrics_by_group_list

        out["efficiencyMetricsByGroup"] = (
            capo_cost_optimization_hub.types.efficiency_metrics_by_group_list.serialize_aws_json_1_0(
                value["efficiency_metrics_by_group"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEfficiencyMetricsResponse:
    out: ListEfficiencyMetricsResponse = {}  # type: ignore[typeddict-item]
    if "efficiencyMetricsByGroup" in data:
        import capo_cost_optimization_hub.types.efficiency_metrics_by_group_list

        out["efficiency_metrics_by_group"] = (
            capo_cost_optimization_hub.types.efficiency_metrics_by_group_list.deserialize_aws_json_1_0(
                data["efficiencyMetricsByGroup"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
