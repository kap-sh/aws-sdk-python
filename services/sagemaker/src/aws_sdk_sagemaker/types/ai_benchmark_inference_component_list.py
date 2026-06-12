"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIBenchmarkInferenceComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ai_benchmark_inference_component

AIBenchmarkInferenceComponentList: TypeAlias = list[
    "aws_sdk_sagemaker.types.ai_benchmark_inference_component.AIBenchmarkInferenceComponent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIBenchmarkInferenceComponentList) -> list:
    import aws_sdk_sagemaker.types.ai_benchmark_inference_component

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.ai_benchmark_inference_component.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AIBenchmarkInferenceComponentList:
    import aws_sdk_sagemaker.types.ai_benchmark_inference_component

    out: AIBenchmarkInferenceComponentList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.ai_benchmark_inference_component.deserialize_aws_json_1_1(
                item
            )
        )
    return out
