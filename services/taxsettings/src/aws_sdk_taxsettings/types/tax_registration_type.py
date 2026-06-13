"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "VAT",
        "GST",
        "CPF",
        "CNPJ",
        "SST",
        "TIN",
        "NRIC",
        "PAN",
        "NIP",
    )
)


def serialize_json(value: TaxRegistrationType) -> str:
    return value


def deserialize_json(data: str) -> TaxRegistrationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaxRegistrationType value: {data!r}")
    return cast(TaxRegistrationType, data)
