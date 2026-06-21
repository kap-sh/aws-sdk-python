"""Generated from Smithy shape ``com.amazonaws.taxsettings#Sector``."""

from typing import Literal, TypeAlias, cast

Sector: TypeAlias = Literal[
    "Business",
    "Individual",
    "Government",
]


# --- restJson1 ser/de ---
def serialize_json(value: Sector) -> str:
    return value


def deserialize_json(data: str) -> Sector:
    return cast(Sector, data)
