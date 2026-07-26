"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelVersionType``."""

from typing import Literal, TypeAlias, cast

AssetModelVersionType: TypeAlias = Literal[
    "LATEST",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelVersionType) -> str:
    return value


def deserialize_json(data: str) -> AssetModelVersionType:
    return cast(AssetModelVersionType, data)
