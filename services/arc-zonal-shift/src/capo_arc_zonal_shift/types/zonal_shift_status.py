"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ZonalShiftStatus``."""

from typing import Literal, TypeAlias, cast

ZonalShiftStatus: TypeAlias = Literal[
    "ACTIVE",
    "EXPIRED",
    "CANCELED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ZonalShiftStatus) -> str:
    return value


def deserialize_json(data: str) -> ZonalShiftStatus:
    return cast(ZonalShiftStatus, data)
