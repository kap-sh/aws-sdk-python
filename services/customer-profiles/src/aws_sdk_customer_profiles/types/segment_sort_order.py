"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SegmentSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

SegmentSortOrder: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def serialize_json(value: SegmentSortOrder) -> str:
    return value


def deserialize_json(data: str) -> SegmentSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SegmentSortOrder value: {data!r}")
    return cast(SegmentSortOrder, data)
