"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsEbifControl``."""

from typing import Literal, TypeAlias, cast

"""M2ts Ebif Control"""
M2tsEbifControl: TypeAlias = Literal[
    "NONE",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: M2tsEbifControl) -> str:
    return value


def deserialize_json(data: str) -> M2tsEbifControl:
    return cast(M2tsEbifControl, data)
