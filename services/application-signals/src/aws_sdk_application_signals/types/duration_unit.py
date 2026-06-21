"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DurationUnit``."""

from typing import Literal, TypeAlias, cast

DurationUnit: TypeAlias = Literal[
    "MINUTE",
    "HOUR",
    "DAY",
    "MONTH",
]


# --- restJson1 ser/de ---
def serialize_json(value: DurationUnit) -> str:
    return value


def deserialize_json(data: str) -> DurationUnit:
    return cast(DurationUnit, data)
