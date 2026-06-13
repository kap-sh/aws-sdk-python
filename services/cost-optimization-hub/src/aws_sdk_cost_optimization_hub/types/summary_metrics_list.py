"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#SummaryMetricsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_optimization_hub.types.summary_metrics

SummaryMetricsList: TypeAlias = list[
    "aws_sdk_cost_optimization_hub.types.summary_metrics.SummaryMetrics"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SummaryMetricsList) -> list:
    import aws_sdk_cost_optimization_hub.types.summary_metrics

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_optimization_hub.types.summary_metrics.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SummaryMetricsList:
    import aws_sdk_cost_optimization_hub.types.summary_metrics

    out: SummaryMetricsList = []
    for item in data:
        out.append(
            aws_sdk_cost_optimization_hub.types.summary_metrics.deserialize_aws_json_1_0(
                item
            )
        )
    return out
