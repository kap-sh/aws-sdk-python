"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileTypeDimensionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

ProfileTypeDimensionType: TypeAlias = Literal[
    "INCLUSIVE",
    "EXCLUSIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INCLUSIVE",
        "EXCLUSIVE",
    )
)


def serialize_json(value: ProfileTypeDimensionType) -> str:
    return value


def deserialize_json(data: str) -> ProfileTypeDimensionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfileTypeDimensionType value: {data!r}")
    return cast(ProfileTypeDimensionType, data)
