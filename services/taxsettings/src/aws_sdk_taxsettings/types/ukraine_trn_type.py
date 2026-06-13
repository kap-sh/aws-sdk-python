"""Generated from Smithy shape ``com.amazonaws.taxsettings#UkraineTrnType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

UkraineTrnType: TypeAlias = Literal[
    "Business",
    "Individual",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Business",
        "Individual",
    )
)


def serialize_json(value: UkraineTrnType) -> str:
    return value


def deserialize_json(data: str) -> UkraineTrnType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UkraineTrnType value: {data!r}")
    return cast(UkraineTrnType, data)
