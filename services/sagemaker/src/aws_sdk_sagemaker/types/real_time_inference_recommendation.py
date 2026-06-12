"""Generated from Smithy shape ``com.amazonaws.sagemaker#RealTimeInferenceRecommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.environment_map
    import aws_sdk_sagemaker.types.production_variant_instance_type
    import aws_sdk_sagemaker.types.string


class RealTimeInferenceRecommendation(TypedDict):
    recommendation_id: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The recommendation ID which uniquely identifies each recommendation.</p>"""
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_instance_type.ProductionVariantInstanceType"
    ]
    """<p>The recommended instance type for Real-Time Inference.</p>"""
    environment: NotRequired["aws_sdk_sagemaker.types.environment_map.EnvironmentMap"]
    """<p>The recommended environment variables to set in the model container for Real-Time Inference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RealTimeInferenceRecommendation) -> dict:
    out: dict = {}
    if "recommendation_id" in value:
        out["RecommendationId"] = value["recommendation_id"]
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.production_variant_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.production_variant_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "environment" in value:
        import aws_sdk_sagemaker.types.environment_map

        out["Environment"] = (
            aws_sdk_sagemaker.types.environment_map.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RealTimeInferenceRecommendation:
    out: RealTimeInferenceRecommendation = {}  # type: ignore[typeddict-item]
    if "RecommendationId" in data:
        out["recommendation_id"] = data["RecommendationId"]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.production_variant_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.production_variant_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "Environment" in data:
        import aws_sdk_sagemaker.types.environment_map

        out["environment"] = (
            aws_sdk_sagemaker.types.environment_map.deserialize_aws_json_1_1(
                data["Environment"]
            )
        )
    return out
