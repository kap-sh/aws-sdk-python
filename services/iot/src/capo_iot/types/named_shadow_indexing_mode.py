"""Generated from Smithy shape ``com.amazonaws.iot#NamedShadowIndexingMode``."""

from typing import Literal, TypeAlias, cast

NamedShadowIndexingMode: TypeAlias = Literal[
    "OFF",
    "ON",
]


# --- restJson1 ser/de ---
def serialize_json(value: NamedShadowIndexingMode) -> str:
    return value


def deserialize_json(data: str) -> NamedShadowIndexingMode:
    return cast(NamedShadowIndexingMode, data)
