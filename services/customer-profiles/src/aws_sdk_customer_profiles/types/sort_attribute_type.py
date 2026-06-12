"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SortAttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

SortAttributeType: TypeAlias = Literal[
    "PROFILE",
    "CALCULATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROFILE",
        "CALCULATED",
    )
)


def serialize_json(value: SortAttributeType) -> str:
    return value


def deserialize_json(data: str) -> SortAttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortAttributeType value: {data!r}")
    return cast(SortAttributeType, data)
