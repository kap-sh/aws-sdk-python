"""Generated from Smithy shape ``com.amazonaws.taxsettings#PolandTaxRegistrationNumberType``."""

from typing import Literal, TypeAlias, cast

PolandTaxRegistrationNumberType: TypeAlias = Literal[
    "EUTaxRegistrationNumber",
    "LocalTaxRegistrationNumber",
    "LocalRegistrationNumber",
]


# --- restJson1 ser/de ---
def serialize_json(value: PolandTaxRegistrationNumberType) -> str:
    return value


def deserialize_json(data: str) -> PolandTaxRegistrationNumberType:
    return cast(PolandTaxRegistrationNumberType, data)
