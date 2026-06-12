"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TimeOrdering``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

TimeOrdering: TypeAlias = Literal[
    "ASCENDING",
    "DESCENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASCENDING",
        "DESCENDING",
    )
)


def serialize_json(value: TimeOrdering) -> str:
    return value


def deserialize_json(data: str) -> TimeOrdering:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TimeOrdering value: {data!r}")
    return cast(TimeOrdering, data)
