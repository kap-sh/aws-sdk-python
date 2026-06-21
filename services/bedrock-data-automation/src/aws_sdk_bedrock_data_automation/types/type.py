"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#Type``."""

from typing import Literal, TypeAlias, cast

"""Type"""
Type: TypeAlias = Literal[
    "DOCUMENT",
    "IMAGE",
    "AUDIO",
    "VIDEO",
]


# --- restJson1 ser/de ---
def serialize_json(value: Type) -> str:
    return value


def deserialize_json(data: str) -> Type:
    return cast(Type, data)
