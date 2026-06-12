"""Generated from Smithy shape ``com.amazonaws.pinpoint#SegmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

SegmentType: TypeAlias = Literal[
    "DIMENSIONAL",
    "IMPORT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIMENSIONAL",
        "IMPORT",
    )
)


def serialize_json(value: SegmentType) -> str:
    return value


def deserialize_json(data: str) -> SegmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SegmentType value: {data!r}")
    return cast(SegmentType, data)
