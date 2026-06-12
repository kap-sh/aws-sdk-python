"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Quality``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

Quality: TypeAlias = Literal[
    "GOOD",
    "BAD",
    "UNCERTAIN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GOOD",
        "BAD",
        "UNCERTAIN",
    )
)


def serialize_json(value: Quality) -> str:
    return value


def deserialize_json(data: str) -> Quality:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Quality value: {data!r}")
    return cast(Quality, data)
