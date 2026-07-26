"""Generated from Smithy shape ``com.amazonaws.glue#CompactionStrategy``."""

from typing import Literal, TypeAlias, cast

CompactionStrategy: TypeAlias = Literal[
    "binpack",
    "sort",
    "z-order",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompactionStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompactionStrategy:
    return cast(CompactionStrategy, data)
