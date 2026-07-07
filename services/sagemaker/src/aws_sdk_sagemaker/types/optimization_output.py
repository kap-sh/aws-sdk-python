"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.optimization_container_image


class OptimizationOutput(TypedDict, closed=True):
    recommended_inference_image: NotRequired[
        "aws_sdk_sagemaker.types.optimization_container_image.OptimizationContainerImage"
    ]
    """<p>The image that SageMaker recommends that you use to host the optimized model that you created with an optimization job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationOutput) -> dict:
    out: dict = {}
    if "recommended_inference_image" in value:
        out["RecommendedInferenceImage"] = value["recommended_inference_image"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OptimizationOutput:
    out: OptimizationOutput = {}  # type: ignore[typeddict-item]
    if "RecommendedInferenceImage" in data:
        out["recommended_inference_image"] = data["RecommendedInferenceImage"]
    return out
