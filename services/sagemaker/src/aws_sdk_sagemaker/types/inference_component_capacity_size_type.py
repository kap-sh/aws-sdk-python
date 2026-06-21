"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentCapacitySizeType``."""

from typing import Literal, TypeAlias, cast

InferenceComponentCapacitySizeType: TypeAlias = Literal[
    "COPY_COUNT",
    "CAPACITY_PERCENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentCapacitySizeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceComponentCapacitySizeType:
    return cast(InferenceComponentCapacitySizeType, data)
