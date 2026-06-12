"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentRuntimeConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_component_copy_count


class InferenceComponentRuntimeConfig(TypedDict):
    copy_count: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_copy_count.InferenceComponentCopyCount"
    ]
    """<p>The number of runtime copies of the model container to deploy with the inference component. Each copy can serve inference requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentRuntimeConfig) -> dict:
    out: dict = {}
    if "copy_count" in value:
        out["CopyCount"] = value["copy_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentRuntimeConfig:
    out: InferenceComponentRuntimeConfig = {}  # type: ignore[typeddict-item]
    if "CopyCount" in data:
        out["copy_count"] = data["CopyCount"]
    return out
