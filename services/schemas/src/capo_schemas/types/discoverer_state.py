"""Generated from Smithy shape ``com.amazonaws.schemas#DiscovererState``."""

from typing import Literal, TypeAlias, cast

DiscovererState: TypeAlias = Literal[
    "STARTED",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DiscovererState) -> str:
    return value


def deserialize_json(data: str) -> DiscovererState:
    return cast(DiscovererState, data)
