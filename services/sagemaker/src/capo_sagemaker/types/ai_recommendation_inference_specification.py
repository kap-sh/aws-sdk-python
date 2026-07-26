"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationInferenceSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_recommendation_inference_framework


class AIRecommendationInferenceSpecification(TypedDict, closed=True):
    framework: NotRequired[
        "capo_sagemaker.types.ai_recommendation_inference_framework.AIRecommendationInferenceFramework"
    ]
    """<p>The inference framework. Valid values are <code>LMI</code> and <code>VLLM</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationInferenceSpecification) -> dict:
    out: dict = {}
    if "framework" in value:
        import capo_sagemaker.types.ai_recommendation_inference_framework

        out["Framework"] = (
            capo_sagemaker.types.ai_recommendation_inference_framework.serialize_aws_json_1_1(
                value["framework"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationInferenceSpecification:
    out: AIRecommendationInferenceSpecification = {}  # type: ignore[typeddict-item]
    if "Framework" in data:
        import capo_sagemaker.types.ai_recommendation_inference_framework

        out["framework"] = (
            capo_sagemaker.types.ai_recommendation_inference_framework.deserialize_aws_json_1_1(
                data["Framework"]
            )
        )
    return out
