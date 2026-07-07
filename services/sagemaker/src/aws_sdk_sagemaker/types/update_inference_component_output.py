"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateInferenceComponentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_component_arn


class UpdateInferenceComponentOutput(TypedDict, closed=True):
    inference_component_arn: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_arn.InferenceComponentArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the inference component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInferenceComponentOutput) -> dict:
    out: dict = {}
    if "inference_component_arn" in value:
        out["InferenceComponentArn"] = value["inference_component_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInferenceComponentOutput:
    out: UpdateInferenceComponentOutput = {}  # type: ignore[typeddict-item]
    if "InferenceComponentArn" in data:
        out["inference_component_arn"] = data["InferenceComponentArn"]
    return out
