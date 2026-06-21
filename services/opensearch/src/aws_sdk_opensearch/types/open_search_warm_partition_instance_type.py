"""Generated from Smithy shape ``com.amazonaws.opensearch#OpenSearchWarmPartitionInstanceType``."""

from typing import Literal, TypeAlias, cast

OpenSearchWarmPartitionInstanceType: TypeAlias = Literal[
    "ultrawarm1.medium.search",
    "ultrawarm1.large.search",
    "ultrawarm1.xlarge.search",
]


# --- restJson1 ser/de ---
def serialize_json(value: OpenSearchWarmPartitionInstanceType) -> str:
    return value


def deserialize_json(data: str) -> OpenSearchWarmPartitionInstanceType:
    return cast(OpenSearchWarmPartitionInstanceType, data)
