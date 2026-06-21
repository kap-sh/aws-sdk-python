"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ComponentType``."""

from typing import Literal, TypeAlias, cast

ComponentType: TypeAlias = Literal[
    "BUILD",
    "TEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentType) -> str:
    return value


def deserialize_json(data: str) -> ComponentType:
    return cast(ComponentType, data)
