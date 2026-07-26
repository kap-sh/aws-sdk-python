"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIBenchmarkInferenceComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_benchmark_inference_component

AIBenchmarkInferenceComponentList: TypeAlias = list[
    "capo_sagemaker.types.ai_benchmark_inference_component.AIBenchmarkInferenceComponent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIBenchmarkInferenceComponentList) -> list:
    import capo_sagemaker.types.ai_benchmark_inference_component

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.ai_benchmark_inference_component.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIBenchmarkInferenceComponentList:
    import capo_sagemaker.types.ai_benchmark_inference_component

    out: AIBenchmarkInferenceComponentList = []
    for item in data:
        out.append(
            capo_sagemaker.types.ai_benchmark_inference_component.deserialize_aws_json_1_1(
                item
            )
        )
    return out
