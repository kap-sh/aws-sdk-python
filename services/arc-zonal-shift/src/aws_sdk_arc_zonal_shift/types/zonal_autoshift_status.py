"""Generated from Smithy shape ``com.amazonaws.arczonalshift#ZonalAutoshiftStatus``."""

from typing import Literal, TypeAlias, cast

ZonalAutoshiftStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ZonalAutoshiftStatus) -> str:
    return value


def deserialize_json(data: str) -> ZonalAutoshiftStatus:
    return cast(ZonalAutoshiftStatus, data)
