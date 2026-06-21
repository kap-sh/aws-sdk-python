"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetModelState``."""

from typing import Literal, TypeAlias, cast

AssetModelState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "PROPAGATING",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetModelState) -> str:
    return value


def deserialize_json(data: str) -> AssetModelState:
    return cast(AssetModelState, data)
