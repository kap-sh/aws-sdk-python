"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantInferenceAmiVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ProductionVariantInferenceAmiVersion: TypeAlias = Literal[
    "al2-ami-sagemaker-inference-gpu-2",
    "al2-ami-sagemaker-inference-gpu-2-1",
    "al2-ami-sagemaker-inference-gpu-3-1",
    "al2-ami-sagemaker-inference-neuron-2",
    "al2023-ami-sagemaker-inference-gpu-4-1",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "al2-ami-sagemaker-inference-gpu-2",
        "al2-ami-sagemaker-inference-gpu-2-1",
        "al2-ami-sagemaker-inference-gpu-3-1",
        "al2-ami-sagemaker-inference-neuron-2",
        "al2023-ami-sagemaker-inference-gpu-4-1",
    )
)


def serialize_aws_json_1_1(value: ProductionVariantInferenceAmiVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductionVariantInferenceAmiVersion:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProductionVariantInferenceAmiVersion value: {data!r}"
        )
    return cast(ProductionVariantInferenceAmiVersion, data)
