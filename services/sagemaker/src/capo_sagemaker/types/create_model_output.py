"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateModelOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.model_arn


class CreateModelOutput(TypedDict, closed=True):
    model_arn: NotRequired["capo_sagemaker.types.model_arn.ModelArn"]
    """<p>The ARN of the model created in SageMaker.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateModelOutput) -> dict:
    out: dict = {}
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateModelOutput:
    out: CreateModelOutput = {}  # type: ignore[typeddict-item]
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    return out
