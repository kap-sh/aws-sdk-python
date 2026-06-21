"""Generated from Smithy shape ``com.amazonaws.outposts#AssetType``."""

from typing import Literal, TypeAlias, cast

AssetType: TypeAlias = Literal[
    "COMPUTE",
    "STORAGE",
    "POWERSHELF",
    "SWITCH",
    "NETWORKING",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetType) -> str:
    return value


def deserialize_json(data: str) -> AssetType:
    return cast(AssetType, data)
