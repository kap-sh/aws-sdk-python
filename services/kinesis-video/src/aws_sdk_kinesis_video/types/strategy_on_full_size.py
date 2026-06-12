"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#StrategyOnFullSize``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

StrategyOnFullSize: TypeAlias = Literal[
    "DELETE_OLDEST_MEDIA",
    "DENY_NEW_MEDIA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELETE_OLDEST_MEDIA",
        "DENY_NEW_MEDIA",
    )
)


def serialize_json(value: StrategyOnFullSize) -> str:
    return value


def deserialize_json(data: str) -> StrategyOnFullSize:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StrategyOnFullSize value: {data!r}")
    return cast(StrategyOnFullSize, data)
