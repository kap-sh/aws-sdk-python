"""Generated from Smithy shape ``com.amazonaws.glue#ComputeEnvironment``."""

from typing import Literal, TypeAlias, cast

ComputeEnvironment: TypeAlias = Literal[
    "SPARK",
    "ATHENA",
    "PYTHON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputeEnvironment) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputeEnvironment:
    return cast(ComputeEnvironment, data)
