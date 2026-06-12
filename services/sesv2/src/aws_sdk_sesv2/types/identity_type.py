"""Generated from Smithy shape ``com.amazonaws.sesv2#IdentityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

IdentityType: TypeAlias = Literal[
    "EMAIL_ADDRESS",
    "DOMAIN",
    "MANAGED_DOMAIN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMAIL_ADDRESS",
        "DOMAIN",
        "MANAGED_DOMAIN",
    )
)


def serialize_json(value: IdentityType) -> str:
    return value


def deserialize_json(data: str) -> IdentityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentityType value: {data!r}")
    return cast(IdentityType, data)
