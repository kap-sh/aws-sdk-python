"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationInstanceDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation_copy_count_per_instance
    import aws_sdk_sagemaker.types.ai_recommendation_instance_count
    import aws_sdk_sagemaker.types.ai_recommendation_instance_type


class AIRecommendationInstanceDetail(TypedDict):
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_instance_type.AIRecommendationInstanceType"
    ]
    """<p>The recommended instance type.</p>"""
    instance_count: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_instance_count.AIRecommendationInstanceCount"
    ]
    """<p>The recommended number of instances.</p>"""
    copy_count_per_instance: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_copy_count_per_instance.AIRecommendationCopyCountPerInstance"
    ]
    """<p>The number of model copies per instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationInstanceDetail) -> dict:
    out: dict = {}
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
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationInstanceDetail:
    out: AIRecommendationInstanceDetail = {}  # type: ignore[typeddict-item]
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
    return out
