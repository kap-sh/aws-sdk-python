"""Generated from Smithy shape ``com.amazonaws.taxsettings#SaudiArabiaTaxRegistrationNumberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

SaudiArabiaTaxRegistrationNumberType: TypeAlias = Literal[
    "TaxRegistrationNumber",
    "TaxIdentificationNumber",
    "CommercialRegistrationNumber",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TaxRegistrationNumber",
        "TaxIdentificationNumber",
        "CommercialRegistrationNumber",
    )
)


def serialize_json(value: SaudiArabiaTaxRegistrationNumberType) -> str:
    return value


def deserialize_json(data: str) -> SaudiArabiaTaxRegistrationNumberType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SaudiArabiaTaxRegistrationNumberType value: {data!r}"
        )
    return cast(SaudiArabiaTaxRegistrationNumberType, data)
