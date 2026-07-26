"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationDeploymentS3ChannelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_recommendation_deployment_s3_channel

AIRecommendationDeploymentS3ChannelList: TypeAlias = list[
    "capo_sagemaker.types.ai_recommendation_deployment_s3_channel.AIRecommendationDeploymentS3Channel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationDeploymentS3ChannelList) -> list:
    import capo_sagemaker.types.ai_recommendation_deployment_s3_channel

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.ai_recommendation_deployment_s3_channel.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIRecommendationDeploymentS3ChannelList:
    import capo_sagemaker.types.ai_recommendation_deployment_s3_channel

    out: AIRecommendationDeploymentS3ChannelList = []
    for item in data:
        out.append(
            capo_sagemaker.types.ai_recommendation_deployment_s3_channel.deserialize_aws_json_1_1(
                item
            )
        )
    return out
