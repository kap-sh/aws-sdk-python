"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#EfficiencyMetricsByGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.metrics_by_time_list


class EfficiencyMetricsByGroup(TypedDict, closed=True):
    metrics_by_time: NotRequired[
        "aws_sdk_cost_optimization_hub.types.metrics_by_time_list.MetricsByTimeList"
    ]
    """<p>A list of time-series data points containing efficiency metrics for this group. Each data point includes an efficiency score, estimated savings, spending, and a timestamp corresponding to the specified granularity. This field is null when efficiency metrics cannot be calculated for the group, in which case the message field provides an explanation.</p>"""
    group: NotRequired["str"]
    """<p>The value of the grouping dimension for this set of metrics. For example, if grouped by account ID, this field contains the account ID. If no grouping is specified, this field is empty.</p>"""
    message: NotRequired["str"]
    """<p>An explanation of why efficiency metrics could not be calculated for this group when the metricsByTime field is null. Common reasons include insufficient or inconclusive cost and usage data during the specified time period. This field is null or empty when metrics are successfully calculated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EfficiencyMetricsByGroup) -> dict:
    out: dict = {}
    if "metrics_by_time" in value:
        import aws_sdk_cost_optimization_hub.types.metrics_by_time_list

        out["metricsByTime"] = (
            aws_sdk_cost_optimization_hub.types.metrics_by_time_list.serialize_aws_json_1_0(
                value["metrics_by_time"]
            )
        )
    if "group" in value:
        out["group"] = value["group"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EfficiencyMetricsByGroup:
    out: EfficiencyMetricsByGroup = {}  # type: ignore[typeddict-item]
    if "metricsByTime" in data:
        import aws_sdk_cost_optimization_hub.types.metrics_by_time_list

        out["metrics_by_time"] = (
            aws_sdk_cost_optimization_hub.types.metrics_by_time_list.deserialize_aws_json_1_0(
                data["metricsByTime"]
            )
        )
    if "group" in data:
        out["group"] = data["group"]
    if "message" in data:
        out["message"] = data["message"]
    return out
