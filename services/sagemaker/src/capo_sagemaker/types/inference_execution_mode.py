"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceExecutionMode``."""

from typing import Literal, TypeAlias, cast

InferenceExecutionMode: TypeAlias = Literal[
    "Serial",
    "Direct",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceExecutionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceExecutionMode:
    return cast(InferenceExecutionMode, data)
