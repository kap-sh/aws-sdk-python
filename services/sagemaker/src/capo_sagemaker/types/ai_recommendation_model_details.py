"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationModelDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_inference_specification_name
    import capo_sagemaker.types.ai_recommendation_instance_detail_list
    import capo_sagemaker.types.model_package_arn


class AIRecommendationModelDetails(TypedDict, closed=True):
    model_package_arn: NotRequired[
        "capo_sagemaker.types.model_package_arn.ModelPackageArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the model package.</p>"""
    inference_specification_name: NotRequired[
        "capo_sagemaker.types.ai_inference_specification_name.AIInferenceSpecificationName"
    ]
    """<p>The name of the inference specification within the model package.</p>"""
    instance_details: NotRequired[
        "capo_sagemaker.types.ai_recommendation_instance_detail_list.AIRecommendationInstanceDetailList"
    ]
    """<p>The instance details for this recommendation, including instance type, count, and model copies per instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationModelDetails) -> dict:
    out: dict = {}
    if "model_package_arn" in value:
        out["ModelPackageArn"] = value["model_package_arn"]
    if "inference_specification_name" in value:
        out["InferenceSpecificationName"] = value["inference_specification_name"]
    if "instance_details" in value:
        import capo_sagemaker.types.ai_recommendation_instance_detail_list

        out["InstanceDetails"] = (
            capo_sagemaker.types.ai_recommendation_instance_detail_list.serialize_aws_json_1_1(
                value["instance_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationModelDetails:
    out: AIRecommendationModelDetails = {}  # type: ignore[typeddict-item]
    if "ModelPackageArn" in data:
        out["model_package_arn"] = data["ModelPackageArn"]
    if "InferenceSpecificationName" in data:
        out["inference_specification_name"] = data["InferenceSpecificationName"]
    if "InstanceDetails" in data:
        import capo_sagemaker.types.ai_recommendation_instance_detail_list

        out["instance_details"] = (
            capo_sagemaker.types.ai_recommendation_instance_detail_list.deserialize_aws_json_1_1(
                data["InstanceDetails"]
            )
        )
    return out
