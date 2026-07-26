"""Generated from Smithy shape ``com.amazonaws.resiliencehub#CostFrequency``."""

from typing import Literal, TypeAlias, cast

CostFrequency: TypeAlias = Literal[
    "Hourly",
    "Daily",
    "Monthly",
    "Yearly",
]


# --- restJson1 ser/de ---
def serialize_json(value: CostFrequency) -> str:
    return value


def deserialize_json(data: str) -> CostFrequency:
    return cast(CostFrequency, data)
