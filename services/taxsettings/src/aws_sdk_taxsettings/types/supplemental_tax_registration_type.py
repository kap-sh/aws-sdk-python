"""Generated from Smithy shape ``com.amazonaws.taxsettings#SupplementalTaxRegistrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

SupplementalTaxRegistrationType: TypeAlias = Literal["VAT",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("VAT",))


def serialize_json(value: SupplementalTaxRegistrationType) -> str:
    return value


def deserialize_json(data: str) -> SupplementalTaxRegistrationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SupplementalTaxRegistrationType value: {data!r}"
        )
    return cast(SupplementalTaxRegistrationType, data)
