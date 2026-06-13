"""Generated from Smithy shape ``com.amazonaws.taxsettings#IndonesiaTaxRegistrationNumberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

IndonesiaTaxRegistrationNumberType: TypeAlias = Literal[
    "NIK",
    "PassportNumber",
    "NPWP",
    "NITKU",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NIK",
        "PassportNumber",
        "NPWP",
        "NITKU",
    )
)


def serialize_json(value: IndonesiaTaxRegistrationNumberType) -> str:
    return value


def deserialize_json(data: str) -> IndonesiaTaxRegistrationNumberType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown IndonesiaTaxRegistrationNumberType value: {data!r}"
        )
    return cast(IndonesiaTaxRegistrationNumberType, data)
