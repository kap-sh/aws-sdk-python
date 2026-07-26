"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ECSServiceRecommendationFindingReasonCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_code

ECSServiceRecommendationFindingReasonCodes: TypeAlias = list[
    "capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_code.ECSServiceRecommendationFindingReasonCode"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ECSServiceRecommendationFindingReasonCodes) -> list:
    import capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_code

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_code.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ECSServiceRecommendationFindingReasonCodes:
    import capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_code

    out: ECSServiceRecommendationFindingReasonCodes = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.ecs_service_recommendation_finding_reason_code.deserialize_aws_json_1_0(
                item
            )
        )
    return out
