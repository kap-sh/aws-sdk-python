"""Generated from Smithy shape ``com.amazonaws.efs#PerformanceMode``."""

from typing import Literal, TypeAlias, cast

PerformanceMode: TypeAlias = Literal[
    "generalPurpose",
    "maxIO",
]


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceMode) -> str:
    return value


def deserialize_json(data: str) -> PerformanceMode:
    return cast(PerformanceMode, data)
