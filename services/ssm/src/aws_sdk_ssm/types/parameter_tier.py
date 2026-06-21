"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterTier``."""

from typing import Literal, TypeAlias, cast

ParameterTier: TypeAlias = Literal[
    "Standard",
    "Advanced",
    "Intelligent-Tiering",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterTier) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ParameterTier:
    return cast(ParameterTier, data)
