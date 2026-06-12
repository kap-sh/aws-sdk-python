"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteInferenceComponentInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_component_name


class DeleteInferenceComponentInput(TypedDict):
    inference_component_name: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_name.InferenceComponentName"
    ]
    """<p>The name of the inference component to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteInferenceComponentInput) -> dict:
    out: dict = {}
    if "inference_component_name" in value:
        out["InferenceComponentName"] = value["inference_component_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteInferenceComponentInput:
    out: DeleteInferenceComponentInput = {}  # type: ignore[typeddict-item]
    if "InferenceComponentName" in data:
        out["inference_component_name"] = data["InferenceComponentName"]
    return out
