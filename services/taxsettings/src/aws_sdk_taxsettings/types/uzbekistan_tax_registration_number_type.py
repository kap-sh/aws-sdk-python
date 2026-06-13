"""Generated from Smithy shape ``com.amazonaws.taxsettings#UzbekistanTaxRegistrationNumberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

UzbekistanTaxRegistrationNumberType: TypeAlias = Literal[
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


def serialize_json(value: UzbekistanTaxRegistrationNumberType) -> str:
    return value


def deserialize_json(data: str) -> UzbekistanTaxRegistrationNumberType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown UzbekistanTaxRegistrationNumberType value: {data!r}"
        )
    return cast(UzbekistanTaxRegistrationNumberType, data)
