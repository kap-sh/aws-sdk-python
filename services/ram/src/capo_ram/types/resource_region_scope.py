"""Generated from Smithy shape ``com.amazonaws.ram#ResourceRegionScope``."""

from typing import Literal, TypeAlias, cast

ResourceRegionScope: TypeAlias = Literal[
    "REGIONAL",
    "GLOBAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceRegionScope) -> str:
    return value


def deserialize_json(data: str) -> ResourceRegionScope:
    return cast(ResourceRegionScope, data)
