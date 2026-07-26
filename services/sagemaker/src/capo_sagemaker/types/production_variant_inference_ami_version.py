"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantInferenceAmiVersion``."""

from typing import Literal, TypeAlias, cast

ProductionVariantInferenceAmiVersion: TypeAlias = Literal[
    "al2-ami-sagemaker-inference-gpu-2",
    "al2-ami-sagemaker-inference-gpu-2-1",
    "al2-ami-sagemaker-inference-gpu-3-1",
    "al2-ami-sagemaker-inference-neuron-2",
    "al2023-ami-sagemaker-inference-gpu-4-1",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantInferenceAmiVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductionVariantInferenceAmiVersion:
    return cast(ProductionVariantInferenceAmiVersion, data)
