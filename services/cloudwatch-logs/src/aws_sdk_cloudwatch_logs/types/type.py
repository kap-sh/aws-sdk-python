"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Type``."""

from typing import Literal, TypeAlias, cast

Type: TypeAlias = Literal[
    "boolean",
    "integer",
    "double",
    "string",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Type) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Type:
    return cast(Type, data)
