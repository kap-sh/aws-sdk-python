"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StringDimensionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

StringDimensionType: TypeAlias = Literal[
    "INCLUSIVE",
    "EXCLUSIVE",
    "CONTAINS",
    "BEGINS_WITH",
    "ENDS_WITH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUSIVE",
        "EXCLUSIVE",
        "CONTAINS",
        "BEGINS_WITH",
        "ENDS_WITH",
    )
)


def serialize_json(value: StringDimensionType) -> str:
    return value


def deserialize_json(data: str) -> StringDimensionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StringDimensionType value: {data!r}")
    return cast(StringDimensionType, data)
