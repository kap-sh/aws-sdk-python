"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIBenchmarkEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_benchmark_inference_component_list
    import capo_sagemaker.types.ai_resource_identifier
    import capo_sagemaker.types.string


class AIBenchmarkEndpoint(TypedDict, closed=True):
    identifier: NotRequired[
        "capo_sagemaker.types.ai_resource_identifier.AIResourceIdentifier"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the SageMaker endpoint to benchmark.</p>"""
    target_container_hostname: NotRequired["capo_sagemaker.types.string.String"]
    """<p>The hostname of the specific container to target within a multi-container endpoint.</p>"""
    inference_components: NotRequired[
        "capo_sagemaker.types.ai_benchmark_inference_component_list.AIBenchmarkInferenceComponentList"
    ]
    """<p>The list of inference components to benchmark on the endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIBenchmarkEndpoint) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "target_container_hostname" in value:
        out["TargetContainerHostname"] = value["target_container_hostname"]
    if "inference_components" in value:
        import capo_sagemaker.types.ai_benchmark_inference_component_list

        out["InferenceComponents"] = (
            capo_sagemaker.types.ai_benchmark_inference_component_list.serialize_aws_json_1_1(
                value["inference_components"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIBenchmarkEndpoint:
    out: AIBenchmarkEndpoint = {}  # type: ignore[typeddict-item]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "TargetContainerHostname" in data:
        out["target_container_hostname"] = data["TargetContainerHostname"]
    if "InferenceComponents" in data:
        import capo_sagemaker.types.ai_benchmark_inference_component_list

        out["inference_components"] = (
            capo_sagemaker.types.ai_benchmark_inference_component_list.deserialize_aws_json_1_1(
                data["InferenceComponents"]
            )
        )
    return out
