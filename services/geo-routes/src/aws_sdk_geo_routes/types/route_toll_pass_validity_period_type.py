"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPassValidityPeriodType``."""

from typing import Literal, TypeAlias, cast

RouteTollPassValidityPeriodType: TypeAlias = Literal[
    "Annual",
    "Days",
    "ExtendedAnnual",
    "Minutes",
    "Months",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPassValidityPeriodType) -> str:
    return value


def deserialize_json(data: str) -> RouteTollPassValidityPeriodType:
    return cast(RouteTollPassValidityPeriodType, data)
