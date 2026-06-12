"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationInstanceDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation_instance_detail

AIRecommendationInstanceDetailList: TypeAlias = list[
    "aws_sdk_sagemaker.types.ai_recommendation_instance_detail.AIRecommendationInstanceDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationInstanceDetailList) -> list:
    import aws_sdk_sagemaker.types.ai_recommendation_instance_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.ai_recommendation_instance_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIRecommendationInstanceDetailList:
    import aws_sdk_sagemaker.types.ai_recommendation_instance_detail

    out: AIRecommendationInstanceDetailList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.ai_recommendation_instance_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
