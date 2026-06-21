"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DurationUnits``."""

from typing import Literal, TypeAlias, cast

DurationUnits: TypeAlias = Literal["MONTHS",]


# --- restJson1 ser/de ---
def serialize_json(value: DurationUnits) -> str:
    return value


def deserialize_json(data: str) -> DurationUnits:
    return cast(DurationUnits, data)
