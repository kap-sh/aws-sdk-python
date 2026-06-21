"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetState``."""

from typing import Literal, TypeAlias, cast

AssetState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetState) -> str:
    return value


def deserialize_json(data: str) -> AssetState:
    return cast(AssetState, data)
