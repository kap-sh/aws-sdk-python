"""Generated from Smithy shape ``com.amazonaws.odb#ShapeType``."""

from typing import Literal, TypeAlias, cast

ShapeType: TypeAlias = Literal[
    "AMD",
    "INTEL",
    "INTEL_FLEX_X9",
    "AMPERE_FLEX_A1",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ShapeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ShapeType:
    return cast(ShapeType, data)
