"""Generated from Smithy shape ``com.amazonaws.ram#ResourceRegionScopeFilter``."""

from typing import Literal, TypeAlias, cast

ResourceRegionScopeFilter: TypeAlias = Literal[
    "ALL",
    "REGIONAL",
    "GLOBAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceRegionScopeFilter) -> str:
    return value


def deserialize_json(data: str) -> ResourceRegionScopeFilter:
    return cast(ResourceRegionScopeFilter, data)
