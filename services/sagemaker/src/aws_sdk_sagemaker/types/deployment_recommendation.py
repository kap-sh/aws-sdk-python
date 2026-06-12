"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeploymentRecommendation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.real_time_inference_recommendations
    import aws_sdk_sagemaker.types.recommendation_status


class DeploymentRecommendation(TypedDict):
    recommendation_status: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_status.RecommendationStatus"
    ]
    """<p>Status of the deployment recommendation. The status <code>NOT_APPLICABLE</code> means that SageMaker is unable to provide a default recommendation for the model using the information provided. If the deployment status is <code>IN_PROGRESS</code>, retry your API call after a few seconds to get a <code>COMPLETED</code> deployment recommendation.</p>"""
    real_time_inference_recommendations: NotRequired[
        "aws_sdk_sagemaker.types.real_time_inference_recommendations.RealTimeInferenceRecommendations"
    ]
    """<p>A list of <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_RealTimeInferenceRecommendation.html\">RealTimeInferenceRecommendation</a> items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentRecommendation) -> dict:
    out: dict = {}
    if "recommendation_status" in value:
        import aws_sdk_sagemaker.types.recommendation_status

        out["RecommendationStatus"] = (
            aws_sdk_sagemaker.types.recommendation_status.serialize_aws_json_1_1(
                value["recommendation_status"]
            )
        )
    if "real_time_inference_recommendations" in value:
        import aws_sdk_sagemaker.types.real_time_inference_recommendations

        out["RealTimeInferenceRecommendations"] = (
            aws_sdk_sagemaker.types.real_time_inference_recommendations.serialize_aws_json_1_1(
                value["real_time_inference_recommendations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeploymentRecommendation:
    out: DeploymentRecommendation = {}  # type: ignore[typeddict-item]
    if "RecommendationStatus" in data:
        import aws_sdk_sagemaker.types.recommendation_status

        out["recommendation_status"] = (
            aws_sdk_sagemaker.types.recommendation_status.deserialize_aws_json_1_1(
                data["RecommendationStatus"]
            )
        )
    if "RealTimeInferenceRecommendations" in data:
        import aws_sdk_sagemaker.types.real_time_inference_recommendations

        out["real_time_inference_recommendations"] = (
            aws_sdk_sagemaker.types.real_time_inference_recommendations.deserialize_aws_json_1_1(
                data["RealTimeInferenceRecommendations"]
            )
        )
    return out
