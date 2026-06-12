"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationConstraintList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation_constraint

AIRecommendationConstraintList: TypeAlias = list[
    "aws_sdk_sagemaker.types.ai_recommendation_constraint.AIRecommendationConstraint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationConstraintList) -> list:
    import aws_sdk_sagemaker.types.ai_recommendation_constraint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.ai_recommendation_constraint.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIRecommendationConstraintList:
    import aws_sdk_sagemaker.types.ai_recommendation_constraint

    out: AIRecommendationConstraintList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.ai_recommendation_constraint.deserialize_aws_json_1_1(
                item
            )
        )
    return out
