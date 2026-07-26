"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationOptimizationDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_recommendation_optimization_detail

AIRecommendationOptimizationDetailList: TypeAlias = list[
    "capo_sagemaker.types.ai_recommendation_optimization_detail.AIRecommendationOptimizationDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationOptimizationDetailList) -> list:
    import capo_sagemaker.types.ai_recommendation_optimization_detail

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.ai_recommendation_optimization_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIRecommendationOptimizationDetailList:
    import capo_sagemaker.types.ai_recommendation_optimization_detail

    out: AIRecommendationOptimizationDetailList = []
    for item in data:
        out.append(
            capo_sagemaker.types.ai_recommendation_optimization_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
