"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ESWarmPartitionInstanceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

ESWarmPartitionInstanceType: TypeAlias = Literal[
    "ultrawarm1.medium.elasticsearch",
    "ultrawarm1.large.elasticsearch",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ultrawarm1.medium.elasticsearch",
        "ultrawarm1.large.elasticsearch",
    )
)


def serialize_json(value: ESWarmPartitionInstanceType) -> str:
    return value


def deserialize_json(data: str) -> ESWarmPartitionInstanceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ESWarmPartitionInstanceType value: {data!r}"
        )
    return cast(ESWarmPartitionInstanceType, data)
