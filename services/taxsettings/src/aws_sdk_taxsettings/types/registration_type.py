"""Generated from Smithy shape ``com.amazonaws.taxsettings#RegistrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

RegistrationType: TypeAlias = Literal[
    "Intra-EU",
    "Local",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Intra-EU",
        "Local",
    )
)


def serialize_json(value: RegistrationType) -> str:
    return value


def deserialize_json(data: str) -> RegistrationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegistrationType value: {data!r}")
    return cast(RegistrationType, data)
