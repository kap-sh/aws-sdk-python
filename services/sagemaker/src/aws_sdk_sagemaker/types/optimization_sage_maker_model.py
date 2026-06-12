"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationSageMakerModel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_name


class OptimizationSageMakerModel(TypedDict):
    model_name: NotRequired["aws_sdk_sagemaker.types.model_name.ModelName"]
    """<p>The name of a SageMaker model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationSageMakerModel) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OptimizationSageMakerModel:
    out: OptimizationSageMakerModel = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    return out
