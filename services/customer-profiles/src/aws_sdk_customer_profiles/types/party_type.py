"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PartyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

PartyType: TypeAlias = Literal[
    "INDIVIDUAL",
    "BUSINESS",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INDIVIDUAL",
        "BUSINESS",
        "OTHER",
    )
)


def serialize_json(value: PartyType) -> str:
    return value


def deserialize_json(data: str) -> PartyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PartyType value: {data!r}")
    return cast(PartyType, data)
