"""Generated from Smithy shape ``com.amazonaws.iotsitewise#RawValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

RawValueType: TypeAlias = Literal[
    "D",
    "B",
    "S",
    "I",
    "U",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "D",
        "B",
        "S",
        "I",
        "U",
    )
)


def serialize_json(value: RawValueType) -> str:
    return value


def deserialize_json(data: str) -> RawValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RawValueType value: {data!r}")
    return cast(RawValueType, data)
