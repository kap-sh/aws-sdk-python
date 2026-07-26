"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#UtilizationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.utilization_metric

UtilizationMetrics: TypeAlias = list[
    "capo_compute_optimizer.types.utilization_metric.UtilizationMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UtilizationMetrics) -> list:
    import capo_compute_optimizer.types.utilization_metric

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.utilization_metric.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> UtilizationMetrics:
    import capo_compute_optimizer.types.utilization_metric

    out: UtilizationMetrics = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.utilization_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
