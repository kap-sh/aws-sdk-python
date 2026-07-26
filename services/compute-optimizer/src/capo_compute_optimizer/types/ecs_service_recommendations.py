"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.ecs_service_recommendation

ECSServiceRecommendations: TypeAlias = list[
    "capo_compute_optimizer.types.ecs_service_recommendation.ECSServiceRecommendation"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendations) -> list:
    import capo_compute_optimizer.types.ecs_service_recommendation

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.ecs_service_recommendation.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ECSServiceRecommendations:
    import capo_compute_optimizer.types.ecs_service_recommendation

    out: ECSServiceRecommendations = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.ecs_service_recommendation.deserialize_aws_json_1_0(
                item
            )
        )
    return out
