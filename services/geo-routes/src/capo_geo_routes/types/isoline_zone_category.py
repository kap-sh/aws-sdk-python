"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineZoneCategory``."""

from typing import Literal, TypeAlias, cast

IsolineZoneCategory: TypeAlias = Literal[
    "CongestionPricing",
    "Environmental",
    "Vignette",
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineZoneCategory) -> str:
    return value


def deserialize_json(data: str) -> IsolineZoneCategory:
    return cast(IsolineZoneCategory, data)
