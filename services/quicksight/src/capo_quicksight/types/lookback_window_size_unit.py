"""Generated from Smithy shape ``com.amazonaws.quicksight#LookbackWindowSizeUnit``."""

from typing import Literal, TypeAlias, cast

LookbackWindowSizeUnit: TypeAlias = Literal[
    "HOUR",
    "DAY",
    "WEEK",
]


# --- restJson1 ser/de ---
def serialize_json(value: LookbackWindowSizeUnit) -> str:
    return value


def deserialize_json(data: str) -> LookbackWindowSizeUnit:
    return cast(LookbackWindowSizeUnit, data)
