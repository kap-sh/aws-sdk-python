"""Generated from Smithy shape ``com.amazonaws.glue#ExecutionClass``."""

from typing import Literal, TypeAlias, cast

ExecutionClass: TypeAlias = Literal[
    "FLEX",
    "STANDARD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionClass:
    return cast(ExecutionClass, data)
