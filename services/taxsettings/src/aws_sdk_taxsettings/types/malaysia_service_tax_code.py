"""Generated from Smithy shape ``com.amazonaws.taxsettings#MalaysiaServiceTaxCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

MalaysiaServiceTaxCode: TypeAlias = Literal[
    "Consultancy",
    "Digital Service And Electronic Medium",
    "IT Services",
    "Training Or Coaching",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Consultancy",
        "Digital Service And Electronic Medium",
        "IT Services",
        "Training Or Coaching",
    )
)


def serialize_json(value: MalaysiaServiceTaxCode) -> str:
    return value


def deserialize_json(data: str) -> MalaysiaServiceTaxCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MalaysiaServiceTaxCode value: {data!r}")
    return cast(MalaysiaServiceTaxCode, data)
