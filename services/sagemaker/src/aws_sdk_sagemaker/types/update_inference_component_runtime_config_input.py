"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateInferenceComponentRuntimeConfigInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_component_name
    import aws_sdk_sagemaker.types.inference_component_runtime_config


class UpdateInferenceComponentRuntimeConfigInput(TypedDict):
    inference_component_name: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_name.InferenceComponentName"
    ]
    """<p>The name of the inference component to update.</p>"""
    desired_runtime_config: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_runtime_config.InferenceComponentRuntimeConfig"
    ]
    """<p>Runtime settings for a model that is deployed with an inference component.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateInferenceComponentRuntimeConfigInput) -> dict:
    out: dict = {}
    if "inference_component_name" in value:
        out["InferenceComponentName"] = value["inference_component_name"]
    if "desired_runtime_config" in value:
        import aws_sdk_sagemaker.types.inference_component_runtime_config

        out["DesiredRuntimeConfig"] = (
            aws_sdk_sagemaker.types.inference_component_runtime_config.serialize_aws_json_1_1(
                value["desired_runtime_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateInferenceComponentRuntimeConfigInput:
    out: UpdateInferenceComponentRuntimeConfigInput = {}  # type: ignore[typeddict-item]
    if "InferenceComponentName" in data:
        out["inference_component_name"] = data["InferenceComponentName"]
    if "DesiredRuntimeConfig" in data:
        import aws_sdk_sagemaker.types.inference_component_runtime_config

        out["desired_runtime_config"] = (
            aws_sdk_sagemaker.types.inference_component_runtime_config.deserialize_aws_json_1_1(
                data["DesiredRuntimeConfig"]
            )
        )
    return out
