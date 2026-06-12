"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIRecommendationOptimizationDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_recommendation_optimization_config_map
    import aws_sdk_sagemaker.types.ai_recommendation_optimization_type


class AIRecommendationOptimizationDetail(TypedDict):
    optimization_type: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_optimization_type.AIRecommendationOptimizationType"
    ]
    """<p>The type of optimization. Valid values are <code>SpeculativeDecoding</code> and <code>KernelTuning</code>.</p>"""
    optimization_config: NotRequired[
        "aws_sdk_sagemaker.types.ai_recommendation_optimization_config_map.AIRecommendationOptimizationConfigMap"
    ]
    """<p>A map of configuration parameters for the optimization technique.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIRecommendationOptimizationDetail) -> dict:
    out: dict = {}
    if "optimization_type" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_optimization_type

        out["OptimizationType"] = (
            aws_sdk_sagemaker.types.ai_recommendation_optimization_type.serialize_aws_json_1_1(
                value["optimization_type"]
            )
        )
    if "optimization_config" in value:
        import aws_sdk_sagemaker.types.ai_recommendation_optimization_config_map

        out["OptimizationConfig"] = (
            aws_sdk_sagemaker.types.ai_recommendation_optimization_config_map.serialize_aws_json_1_1(
                value["optimization_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIRecommendationOptimizationDetail:
    out: AIRecommendationOptimizationDetail = {}  # type: ignore[typeddict-item]
    if "OptimizationType" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_optimization_type

        out["optimization_type"] = (
            aws_sdk_sagemaker.types.ai_recommendation_optimization_type.deserialize_aws_json_1_1(
                data["OptimizationType"]
            )
        )
    if "OptimizationConfig" in data:
        import aws_sdk_sagemaker.types.ai_recommendation_optimization_config_map

        out["optimization_config"] = (
            aws_sdk_sagemaker.types.ai_recommendation_optimization_config_map.deserialize_aws_json_1_1(
                data["OptimizationConfig"]
            )
        )
    return out
