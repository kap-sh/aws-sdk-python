"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationDeploymentConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation_copy_count_per_instance
    import aws_sdk_sagemaker.types.ai_recommendation_deployment_s3_channel_list
    import aws_sdk_sagemaker.types.ai_recommendation_instance_count
    import aws_sdk_sagemaker.types.ai_recommendation_instance_type
    import aws_sdk_sagemaker.types.environment_map
    import aws_sdk_sagemaker.types.string


class AIRecommendationDeploymentConfiguration(TypedDict, closed=True):
    s3: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_deployment_s3_channel_list.AIRecommendationDeploymentS3ChannelList"
    ]
    """<p>The Amazon S3 data channels for the deployment.</p>"""
    image_uri: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The URI of the container image for the deployment.</p>"""
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_instance_type.AIRecommendationInstanceType"
    ]
    """<p>The recommended instance type for the deployment.</p>"""
    instance_count: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_instance_count.AIRecommendationInstanceCount"
    ]
    """<p>The recommended number of instances for the deployment.</p>"""
    copy_count_per_instance: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_copy_count_per_instance.AIRecommendationCopyCountPerInstance"
    ]
    """<p>The number of model copies per instance.</p>"""
    environment_variables: NotRequired[
        "aws_sdk_sagemaker.types.environment_map.EnvironmentMap"
    ]
    """<p>The environment variables for the deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationDeploymentConfiguration) -> dict:
    out: dict = {}
    if "s3" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_deployment_s3_channel_list

        out["S3"] = (
            aws_sdk_sagemaker.types.ai_recommendation_deployment_s3_channel_list.serialize_aws_json_1_1(
                value["s3"]
            )
        )
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.ai_recommendation_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "copy_count_per_instance" in value:
        out["CopyCountPerInstance"] = value["copy_count_per_instance"]
    if "environment_variables" in value:
        import aws_sdk_sagemaker.types.environment_map

        out["EnvironmentVariables"] = (
            aws_sdk_sagemaker.types.environment_map.serialize_aws_json_1_1(
                value["environment_variables"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationDeploymentConfiguration:
    out: AIRecommendationDeploymentConfiguration = {}  # type: ignore[typeddict-item]
    if "S3" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_deployment_s3_channel_list

        out["s3"] = (
            aws_sdk_sagemaker.types.ai_recommendation_deployment_s3_channel_list.deserialize_aws_json_1_1(
                data["S3"]
            )
        )
    if "ImageUri" in data:
        out["image_uri"] = data["ImageUri"]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.ai_recommendation_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    if "CopyCountPerInstance" in data:
        out["copy_count_per_instance"] = data["CopyCountPerInstance"]
    if "EnvironmentVariables" in data:
        import aws_sdk_sagemaker.types.environment_map

        out["environment_variables"] = (
            aws_sdk_sagemaker.types.environment_map.deserialize_aws_json_1_1(
                data["EnvironmentVariables"]
            )
        )
    return out
