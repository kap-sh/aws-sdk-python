"""Generated from Smithy shape ``com.amazonaws.signer#ValidityType``."""

from typing import Literal, TypeAlias, cast

ValidityType: TypeAlias = Literal[
    "DAYS",
    "MONTHS",
    "YEARS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidityType) -> str:
    return value


def deserialize_json(data: str) -> ValidityType:
    return cast(ValidityType, data)
