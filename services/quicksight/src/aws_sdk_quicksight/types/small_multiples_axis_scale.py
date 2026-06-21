"""Generated from Smithy shape ``com.amazonaws.quicksight#SmallMultiplesAxisScale``."""

from typing import Literal, TypeAlias, cast

SmallMultiplesAxisScale: TypeAlias = Literal[
    "SHARED",
    "INDEPENDENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SmallMultiplesAxisScale) -> str:
    return value


def deserialize_json(data: str) -> SmallMultiplesAxisScale:
    return cast(SmallMultiplesAxisScale, data)
