"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleUtilizationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.idle_utilization_metric

IdleUtilizationMetrics: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.idle_utilization_metric.IdleUtilizationMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleUtilizationMetrics) -> list:
    import aws_sdk_compute_optimizer.types.idle_utilization_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.idle_utilization_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IdleUtilizationMetrics:
    import aws_sdk_compute_optimizer.types.idle_utilization_metric

    out: IdleUtilizationMetrics = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.idle_utilization_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
