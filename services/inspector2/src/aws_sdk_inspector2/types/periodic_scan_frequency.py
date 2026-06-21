"""Generated from Smithy shape ``com.amazonaws.inspector2#PeriodicScanFrequency``."""

from typing import Literal, TypeAlias, cast

PeriodicScanFrequency: TypeAlias = Literal[
    "WEEKLY",
    "MONTHLY",
    "NEVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: PeriodicScanFrequency) -> str:
    return value


def deserialize_json(data: str) -> PeriodicScanFrequency:
    return cast(PeriodicScanFrequency, data)
