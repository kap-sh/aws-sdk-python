"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#UtilizationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.utilization_metric

UtilizationMetrics: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.utilization_metric.UtilizationMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UtilizationMetrics) -> list:
    import aws_sdk_compute_optimizer.types.utilization_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.utilization_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> UtilizationMetrics:
    import aws_sdk_compute_optimizer.types.utilization_metric

    out: UtilizationMetrics = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.utilization_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
