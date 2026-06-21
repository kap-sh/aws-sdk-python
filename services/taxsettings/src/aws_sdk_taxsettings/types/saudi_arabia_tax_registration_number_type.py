"""Generated from Smithy shape ``com.amazonaws.taxsettings#SaudiArabiaTaxRegistrationNumberType``."""

from typing import Literal, TypeAlias, cast

SaudiArabiaTaxRegistrationNumberType: TypeAlias = Literal[
    "TaxRegistrationNumber",
    "TaxIdentificationNumber",
    "CommercialRegistrationNumber",
]


# --- restJson1 ser/de ---
def serialize_json(value: SaudiArabiaTaxRegistrationNumberType) -> str:
    return value


def deserialize_json(data: str) -> SaudiArabiaTaxRegistrationNumberType:
    return cast(SaudiArabiaTaxRegistrationNumberType, data)
