"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#EfficiencyMetricsByGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.efficiency_metrics_by_group

EfficiencyMetricsByGroupList: TypeAlias = list[
    "aws_sdk_cost_optimization_hub.types.efficiency_metrics_by_group.EfficiencyMetricsByGroup"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EfficiencyMetricsByGroupList) -> list:
    import aws_sdk_cost_optimization_hub.types.efficiency_metrics_by_group

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_optimization_hub.types.efficiency_metrics_by_group.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EfficiencyMetricsByGroupList:
    import aws_sdk_cost_optimization_hub.types.efficiency_metrics_by_group

    out: EfficiencyMetricsByGroupList = []
    for item in data:
        out.append(
            aws_sdk_cost_optimization_hub.types.efficiency_metrics_by_group.deserialize_aws_json_1_0(
                item
            )
        )
    return out
