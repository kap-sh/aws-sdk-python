"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

ProfileType: TypeAlias = Literal[
    "ACCOUNT_PROFILE",
    "PROFILE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT_PROFILE",
        "PROFILE",
    )
)


def serialize_json(value: ProfileType) -> str:
    return value


def deserialize_json(data: str) -> ProfileType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfileType value: {data!r}")
    return cast(ProfileType, data)
