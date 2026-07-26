"""Generated from Smithy shape ``com.amazonaws.medialive#SdiSourceMode``."""

from typing import Literal, TypeAlias, cast

"""Used in SdiSource, CreateSdiSourceRequest, UpdateSdiSourceRequest."""
SdiSourceMode: TypeAlias = Literal[
    "QUADRANT",
    "INTERLEAVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SdiSourceMode) -> str:
    return value


def deserialize_json(data: str) -> SdiSourceMode:
    return cast(SdiSourceMode, data)
