"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PriceUnits``."""

from typing import Literal, TypeAlias, cast

PriceUnits: TypeAlias = Literal["HOURLY",]


# --- restJson1 ser/de ---
def serialize_json(value: PriceUnits) -> str:
    return value


def deserialize_json(data: str) -> PriceUnits:
    return cast(PriceUnits, data)
