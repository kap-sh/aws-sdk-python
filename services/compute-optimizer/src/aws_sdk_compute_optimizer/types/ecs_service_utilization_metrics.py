"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceUtilizationMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.ecs_service_utilization_metric

ECSServiceUtilizationMetrics: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.ecs_service_utilization_metric.ECSServiceUtilizationMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceUtilizationMetrics) -> list:
    import aws_sdk_compute_optimizer.types.ecs_service_utilization_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.ecs_service_utilization_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ECSServiceUtilizationMetrics:
    import aws_sdk_compute_optimizer.types.ecs_service_utilization_metric

    out: ECSServiceUtilizationMetrics = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.ecs_service_utilization_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
