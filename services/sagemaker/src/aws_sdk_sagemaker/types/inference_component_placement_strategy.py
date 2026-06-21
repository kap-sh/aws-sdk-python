"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentPlacementStrategy``."""

from typing import Literal, TypeAlias, cast

InferenceComponentPlacementStrategy: TypeAlias = Literal[
    "SPREAD",
    "BINPACK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentPlacementStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceComponentPlacementStrategy:
    return cast(InferenceComponentPlacementStrategy, data)
