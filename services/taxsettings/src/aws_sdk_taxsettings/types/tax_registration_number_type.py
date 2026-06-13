"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationNumberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

TaxRegistrationNumberType: TypeAlias = Literal[
    "TaxRegistrationNumber",
    "LocalRegistrationNumber",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TaxRegistrationNumber",
        "LocalRegistrationNumber",
    )
)


def serialize_json(value: TaxRegistrationNumberType) -> str:
    return value


def deserialize_json(data: str) -> TaxRegistrationNumberType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaxRegistrationNumberType value: {data!r}")
    return cast(TaxRegistrationNumberType, data)
