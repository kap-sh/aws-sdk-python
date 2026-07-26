"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeLocation``."""

from typing import Literal, TypeAlias, cast

ComputeLocation: TypeAlias = Literal[
    "EDGE",
    "CLOUD",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeLocation) -> str:
    return value


def deserialize_json(data: str) -> ComputeLocation:
    return cast(ComputeLocation, data)
