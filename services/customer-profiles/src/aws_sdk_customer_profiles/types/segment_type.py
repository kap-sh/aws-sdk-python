"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

SegmentType: TypeAlias = Literal[
    "CLASSIC",
    "ENHANCED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLASSIC",
        "ENHANCED",
    )
)


def serialize_json(value: SegmentType) -> str:
    return value


def deserialize_json(data: str) -> SegmentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SegmentType value: {data!r}")
    return cast(SegmentType, data)
