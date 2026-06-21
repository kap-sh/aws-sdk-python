"""Generated from Smithy shape ``com.amazonaws.securityhub#MapFilterComparison``."""

from typing import Literal, TypeAlias, cast

MapFilterComparison: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
    "CONTAINS",
    "NOT_CONTAINS",
]


# --- restJson1 ser/de ---
def serialize_json(value: MapFilterComparison) -> str:
    return value


def deserialize_json(data: str) -> MapFilterComparison:
    return cast(MapFilterComparison, data)
