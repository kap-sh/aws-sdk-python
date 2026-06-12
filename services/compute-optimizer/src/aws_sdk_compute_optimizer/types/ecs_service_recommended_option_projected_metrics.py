"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendedOptionProjectedMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.ecs_service_recommended_option_projected_metric

ECSServiceRecommendedOptionProjectedMetrics: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.ecs_service_recommended_option_projected_metric.ECSServiceRecommendedOptionProjectedMetric"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendedOptionProjectedMetrics) -> list:
    import aws_sdk_compute_optimizer.types.ecs_service_recommended_option_projected_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.ecs_service_recommended_option_projected_metric.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ECSServiceRecommendedOptionProjectedMetrics:
    import aws_sdk_compute_optimizer.types.ecs_service_recommended_option_projected_metric

    out: ECSServiceRecommendedOptionProjectedMetrics = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.ecs_service_recommended_option_projected_metric.deserialize_aws_json_1_0(
                item
            )
        )
    return out
