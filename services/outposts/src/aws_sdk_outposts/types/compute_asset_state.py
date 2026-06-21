"""Generated from Smithy shape ``com.amazonaws.outposts#ComputeAssetState``."""

from typing import Literal, TypeAlias, cast

ComputeAssetState: TypeAlias = Literal[
    "ACTIVE",
    "ISOLATED",
    "RETIRING",
    "INSTALLING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeAssetState) -> str:
    return value


def deserialize_json(data: str) -> ComputeAssetState:
    return cast(ComputeAssetState, data)
