"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ValidityPeriodType``."""

from typing import Literal, TypeAlias, cast

ValidityPeriodType: TypeAlias = Literal[
    "HOURS",
    "DAYS",
    "WEEKS",
    "MONTHS",
    "YEARS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidityPeriodType) -> str:
    return value


def deserialize_json(data: str) -> ValidityPeriodType:
    return cast(ValidityPeriodType, data)
