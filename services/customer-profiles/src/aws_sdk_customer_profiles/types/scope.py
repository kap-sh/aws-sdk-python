"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Scope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

Scope: TypeAlias = Literal[
    "PROFILE",
    "DOMAIN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROFILE",
        "DOMAIN",
    )
)


def serialize_json(value: Scope) -> str:
    return value


def deserialize_json(data: str) -> Scope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Scope value: {data!r}")
    return cast(Scope, data)
