"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationNumberType``."""

from typing import Literal, TypeAlias, cast

TaxRegistrationNumberType: TypeAlias = Literal[
    "TaxRegistrationNumber",
    "LocalRegistrationNumber",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistrationNumberType) -> str:
    return value


def deserialize_json(data: str) -> TaxRegistrationNumberType:
    return cast(TaxRegistrationNumberType, data)
