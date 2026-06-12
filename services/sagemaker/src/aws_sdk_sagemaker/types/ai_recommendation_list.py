"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation

AIRecommendationList: TypeAlias = list[
    "aws_sdk_sagemaker.types.ai_recommendation.AIRecommendation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationList) -> list:
    import aws_sdk_sagemaker.types.ai_recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.ai_recommendation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIRecommendationList:
    import aws_sdk_sagemaker.types.ai_recommendation

    out: AIRecommendationList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.ai_recommendation.deserialize_aws_json_1_1(item)
        )
    return out
