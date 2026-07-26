"""Generated from Smithy shape ``com.amazonaws.taxsettings#UzbekistanTaxRegistrationNumberType``."""

from typing import Literal, TypeAlias, cast

UzbekistanTaxRegistrationNumberType: TypeAlias = Literal[
    "Business",
    "Individual",
]


# --- restJson1 ser/de ---
def serialize_json(value: UzbekistanTaxRegistrationNumberType) -> str:
    return value


def deserialize_json(data: str) -> UzbekistanTaxRegistrationNumberType:
    return cast(UzbekistanTaxRegistrationNumberType, data)
