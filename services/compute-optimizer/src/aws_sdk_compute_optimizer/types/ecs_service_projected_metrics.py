"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceProjectedMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.ecs_service_projected_metric

ECSServiceProjectedMetrics: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.ecs_service_projected_metric.ECSServiceProjectedMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceProjectedMetrics) -> list:
    import aws_sdk_compute_optimizer.types.ecs_service_projected_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.ecs_service_projected_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ECSServiceProjectedMetrics:
    import aws_sdk_compute_optimizer.types.ecs_service_projected_metric

    out: ECSServiceProjectedMetrics = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.ecs_service_projected_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
