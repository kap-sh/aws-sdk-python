"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsNielsenId3Behavior``."""

from typing import Literal, TypeAlias, cast

"""M2ts Nielsen Id3 Behavior"""
M2tsNielsenId3Behavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsNielsenId3Behavior) -> str:
    return value


def deserialize_json(data: str) -> M2tsNielsenId3Behavior:
    return cast(M2tsNielsenId3Behavior, data)
