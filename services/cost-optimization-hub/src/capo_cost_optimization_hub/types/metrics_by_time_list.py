"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#MetricsByTimeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cost_optimization_hub.types.metrics_by_time

MetricsByTimeList: TypeAlias = list[
    "capo_cost_optimization_hub.types.metrics_by_time.MetricsByTime"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricsByTimeList) -> list:
    import capo_cost_optimization_hub.types.metrics_by_time

    out: list = []
    for item in value:
        out.append(
            capo_cost_optimization_hub.types.metrics_by_time.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> MetricsByTimeList:
    import capo_cost_optimization_hub.types.metrics_by_time

    out: MetricsByTimeList = []
    for item in data:
        out.append(
            capo_cost_optimization_hub.types.metrics_by_time.deserialize_aws_json_1_0(
                item
            )
        )
    return out
