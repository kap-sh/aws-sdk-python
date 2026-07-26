"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityOptionType``."""

from typing import Literal, TypeAlias, cast

CapacityOptionType: TypeAlias = Literal[
    "ON_DEMAND",
    "SPOT",
    "RESERVED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityOptionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityOptionType:
    return cast(CapacityOptionType, data)
