"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ESWarmPartitionInstanceType``."""

from typing import Literal, TypeAlias, cast

ESWarmPartitionInstanceType: TypeAlias = Literal[
    "ultrawarm1.medium.elasticsearch",
    "ultrawarm1.large.elasticsearch",
]


# --- restJson1 ser/de ---
def serialize_json(value: ESWarmPartitionInstanceType) -> str:
    return value


def deserialize_json(data: str) -> ESWarmPartitionInstanceType:
    return cast(ESWarmPartitionInstanceType, data)
