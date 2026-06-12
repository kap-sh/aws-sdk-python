"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Order``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. When you request lists of resources, you can specify whether they are sorted in ASCENDING or DESCENDING order. Default varies by resource."""
Order: TypeAlias = Literal[
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


def serialize_json(value: Order) -> str:
    return value


def deserialize_json(data: str) -> Order:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Order value: {data!r}")
    return cast(Order, data)
