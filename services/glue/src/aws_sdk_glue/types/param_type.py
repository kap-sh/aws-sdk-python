"""Generated from Smithy shape ``com.amazonaws.glue#ParamType``."""

from typing import Literal, TypeAlias, cast

ParamType: TypeAlias = Literal[
    "str",
    "int",
    "float",
    "complex",
    "bool",
    "list",
    "null",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParamType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParamType:
    return cast(ParamType, data)
