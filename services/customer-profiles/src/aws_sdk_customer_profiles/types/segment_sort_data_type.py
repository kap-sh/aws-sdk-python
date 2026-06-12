"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentSortDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

SegmentSortDataType: TypeAlias = Literal[
    "STRING",
    "NUMBER",
    "DATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "NUMBER",
        "DATE",
    )
)


def serialize_json(value: SegmentSortDataType) -> str:
    return value


def deserialize_json(data: str) -> SegmentSortDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SegmentSortDataType value: {data!r}")
    return cast(SegmentSortDataType, data)
