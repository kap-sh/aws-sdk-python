"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.ecs_service_recommendation_filter

ECSServiceRecommendationFilters: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.ecs_service_recommendation_filter.ECSServiceRecommendationFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendationFilters) -> list:
    import aws_sdk_compute_optimizer.types.ecs_service_recommendation_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.ecs_service_recommendation_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ECSServiceRecommendationFilters:
    import aws_sdk_compute_optimizer.types.ecs_service_recommendation_filter

    out: ECSServiceRecommendationFilters = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.ecs_service_recommendation_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
