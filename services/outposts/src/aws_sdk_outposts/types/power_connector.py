"""Generated from Smithy shape ``com.amazonaws.outposts#PowerConnector``."""

from typing import Literal, TypeAlias, cast

PowerConnector: TypeAlias = Literal[
    "L6_30P",
    "IEC309",
    "AH530P7W",
    "AH532P6W",
    "CS8365C",
]


# --- restJson1 ser/de ---
def serialize_json(value: PowerConnector) -> str:
    return value


def deserialize_json(data: str) -> PowerConnector:
    return cast(PowerConnector, data)
