"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelType``."""

from typing import Literal, TypeAlias, cast

AssetModelType: TypeAlias = Literal[
    "ASSET_MODEL",
    "COMPONENT_MODEL",
    "INTERFACE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelType) -> str:
    return value


def deserialize_json(data: str) -> AssetModelType:
    return cast(AssetModelType, data)
