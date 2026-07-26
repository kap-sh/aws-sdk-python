"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceExecutionStatus``."""

from typing import Literal, TypeAlias, cast

InferenceExecutionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCESS",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferenceExecutionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InferenceExecutionStatus:
    return cast(InferenceExecutionStatus, data)
