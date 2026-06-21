"""Generated from Smithy shape ``com.amazonaws.codepipeline#ExecutorType``."""

from typing import Literal, TypeAlias, cast

ExecutorType: TypeAlias = Literal[
    "JobWorker",
    "Lambda",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutorType:
    return cast(ExecutorType, data)
