"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationConstraintList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_recommendation_constraint

AIRecommendationConstraintList: TypeAlias = list[
    "capo_sagemaker.types.ai_recommendation_constraint.AIRecommendationConstraint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationConstraintList) -> list:
    import capo_sagemaker.types.ai_recommendation_constraint

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.ai_recommendation_constraint.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIRecommendationConstraintList:
    import capo_sagemaker.types.ai_recommendation_constraint

    out: AIRecommendationConstraintList = []
    for item in data:
        out.append(
            capo_sagemaker.types.ai_recommendation_constraint.deserialize_aws_json_1_1(
                item
            )
        )
    return out
