"""Generated from Smithy shape ``com.amazonaws.outposts#AssetState``."""

from typing import Literal, TypeAlias, cast

AssetState: TypeAlias = Literal[
    "ACTIVE",
    "RETIRING",
    "ISOLATED",
    "INSTALLING",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssetState) -> str:
    return value


def deserialize_json(data: str) -> AssetState:
    return cast(AssetState, data)
