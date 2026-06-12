"""Generated from Smithy shape ``com.amazonaws.customerprofiles#LayoutType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

LayoutType: TypeAlias = Literal["PROFILE_EXPLORER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PROFILE_EXPLORER",))


def serialize_json(value: LayoutType) -> str:
    return value


def deserialize_json(data: str) -> LayoutType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LayoutType value: {data!r}")
    return cast(LayoutType, data)
