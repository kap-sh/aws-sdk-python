"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ShiftType``."""

from typing import Literal, TypeAlias, cast

ShiftType: TypeAlias = Literal[
    "ZONAL_SHIFT",
    "PRACTICE_RUN",
    "FIS_EXPERIMENT",
    "ZONAL_AUTOSHIFT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ShiftType) -> str:
    return value


def deserialize_json(data: str) -> ShiftType:
    return cast(ShiftType, data)
