"""Generated from Smithy shape ``com.amazonaws.taxsettings#PolandTaxRegistrationNumberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

PolandTaxRegistrationNumberType: TypeAlias = Literal[
    "EUTaxRegistrationNumber",
    "LocalTaxRegistrationNumber",
    "LocalRegistrationNumber",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EUTaxRegistrationNumber",
        "LocalTaxRegistrationNumber",
        "LocalRegistrationNumber",
    )
)


def serialize_json(value: PolandTaxRegistrationNumberType) -> str:
    return value


def deserialize_json(data: str) -> PolandTaxRegistrationNumberType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PolandTaxRegistrationNumberType value: {data!r}"
        )
    return cast(PolandTaxRegistrationNumberType, data)
