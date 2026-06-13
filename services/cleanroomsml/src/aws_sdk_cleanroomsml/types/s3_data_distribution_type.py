"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#S3DataDistributionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanroomsml.errors import DeserializationError

S3DataDistributionType: TypeAlias = Literal[
    "FullyReplicated",
    "ShardedByS3Key",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FullyReplicated",
        "ShardedByS3Key",
    )
)


def serialize_json(value: S3DataDistributionType) -> str:
    return value


def deserialize_json(data: str) -> S3DataDistributionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3DataDistributionType value: {data!r}")
    return cast(S3DataDistributionType, data)
