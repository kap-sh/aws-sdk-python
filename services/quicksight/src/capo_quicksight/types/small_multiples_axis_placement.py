"""Generated from Smithy shape ``com.amazonaws.quicksight#SmallMultiplesAxisPlacement``."""

from typing import Literal, TypeAlias, cast

SmallMultiplesAxisPlacement: TypeAlias = Literal[
    "OUTSIDE",
    "INSIDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SmallMultiplesAxisPlacement) -> str:
    return value


def deserialize_json(data: str) -> SmallMultiplesAxisPlacement:
    return cast(SmallMultiplesAxisPlacement, data)
