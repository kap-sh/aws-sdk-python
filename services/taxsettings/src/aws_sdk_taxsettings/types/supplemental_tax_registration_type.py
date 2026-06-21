"""Generated from Smithy shape ``com.amazonaws.taxsettings#SupplementalTaxRegistrationType``."""

from typing import Literal, TypeAlias, cast

SupplementalTaxRegistrationType: TypeAlias = Literal["VAT",]


# --- restJson1 ser/de ---
def serialize_json(value: SupplementalTaxRegistrationType) -> str:
    return value


def deserialize_json(data: str) -> SupplementalTaxRegistrationType:
    return cast(SupplementalTaxRegistrationType, data)
