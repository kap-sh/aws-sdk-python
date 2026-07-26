"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceProjectedUtilizationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.ecs_service_projected_utilization_metric

ECSServiceProjectedUtilizationMetrics: TypeAlias = list[
    "capo_compute_optimizer.types.ecs_service_projected_utilization_metric.ECSServiceProjectedUtilizationMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceProjectedUtilizationMetrics) -> list:
    import capo_compute_optimizer.types.ecs_service_projected_utilization_metric

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.ecs_service_projected_utilization_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ECSServiceProjectedUtilizationMetrics:
    import capo_compute_optimizer.types.ecs_service_projected_utilization_metric

    out: ECSServiceProjectedUtilizationMetrics = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.ecs_service_projected_utilization_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
