"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationInstanceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation_instance_type

AIRecommendationInstanceTypeList: TypeAlias = list[
    "aws_sdk_sagemaker.types.ai_recommendation_instance_type.AIRecommendationInstanceType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationInstanceTypeList) -> list:
    import aws_sdk_sagemaker.types.ai_recommendation_instance_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.ai_recommendation_instance_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIRecommendationInstanceTypeList:
    import aws_sdk_sagemaker.types.ai_recommendation_instance_type

    out: AIRecommendationInstanceTypeList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.ai_recommendation_instance_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
