"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationType``."""

from typing import Literal, TypeAlias, cast

TaxRegistrationType: TypeAlias = Literal[
    "VAT",
    "GST",
    "CPF",
    "CNPJ",
    "SST",
    "TIN",
    "NRIC",
    "PAN",
    "NIP",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistrationType) -> str:
    return value


def deserialize_json(data: str) -> TaxRegistrationType:
    return cast(TaxRegistrationType, data)
