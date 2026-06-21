"""Generated from Smithy shape ``com.amazonaws.forecast#Operation``."""

from typing import Literal, TypeAlias, cast

Operation: TypeAlias = Literal[
    "ADD",
    "SUBTRACT",
    "MULTIPLY",
    "DIVIDE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Operation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Operation:
    return cast(Operation, data)
