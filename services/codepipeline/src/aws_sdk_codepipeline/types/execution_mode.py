"""Generated from Smithy shape ``com.amazonaws.codepipeline#ExecutionMode``."""

from typing import Literal, TypeAlias, cast

ExecutionMode: TypeAlias = Literal[
    "QUEUED",
    "SUPERSEDED",
    "PARALLEL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionMode:
    return cast(ExecutionMode, data)
