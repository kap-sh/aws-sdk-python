"""Generated from Smithy shape ``com.amazonaws.imagebuilder#SsmParameterDataType``."""

from typing import Literal, TypeAlias, cast

SsmParameterDataType: TypeAlias = Literal[
    "text",
    "aws:ec2:image",
]


# --- restJson1 ser/de ---
def serialize_json(value: SsmParameterDataType) -> str:
    return value


def deserialize_json(data: str) -> SsmParameterDataType:
    return cast(SsmParameterDataType, data)
