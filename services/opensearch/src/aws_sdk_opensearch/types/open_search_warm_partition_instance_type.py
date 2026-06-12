"""Generated from Smithy shape ``com.amazonaws.opensearch#OpenSearchWarmPartitionInstanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

OpenSearchWarmPartitionInstanceType: TypeAlias = Literal[
    "ultrawarm1.medium.search",
    "ultrawarm1.large.search",
    "ultrawarm1.xlarge.search",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ultrawarm1.medium.search",
        "ultrawarm1.large.search",
        "ultrawarm1.xlarge.search",
    )
)


def serialize_json(value: OpenSearchWarmPartitionInstanceType) -> str:
    return value


def deserialize_json(data: str) -> OpenSearchWarmPartitionInstanceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OpenSearchWarmPartitionInstanceType value: {data!r}"
        )
    return cast(OpenSearchWarmPartitionInstanceType, data)
