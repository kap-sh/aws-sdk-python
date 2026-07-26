"""Generated from Smithy shape ``com.amazonaws.dax#ParameterType``."""

from typing import Literal, TypeAlias, cast

ParameterType: TypeAlias = Literal[
    "DEFAULT",
    "NODE_TYPE_SPECIFIC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParameterType:
    return cast(ParameterType, data)
