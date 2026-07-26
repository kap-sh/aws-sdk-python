"""Generated from Smithy shape ``com.amazonaws.customerprofiles#PeriodUnit``."""

from typing import Literal, TypeAlias, cast

PeriodUnit: TypeAlias = Literal[
    "MINUTES",
    "HOURS",
    "DAYS",
    "WEEKS",
    "MONTHS",
]


# --- restJson1 ser/de ---
def serialize_json(value: PeriodUnit) -> str:
    return value


def deserialize_json(data: str) -> PeriodUnit:
    return cast(PeriodUnit, data)
