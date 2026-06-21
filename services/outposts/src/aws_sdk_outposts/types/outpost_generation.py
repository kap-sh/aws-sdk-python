"""Generated from Smithy shape ``com.amazonaws.outposts#OutpostGeneration``."""

from typing import Literal, TypeAlias, cast

OutpostGeneration: TypeAlias = Literal[
    "GENERATION_2",
    "GENERATION_1",
]


# --- restJson1 ser/de ---
def serialize_json(value: OutpostGeneration) -> str:
    return value


def deserialize_json(data: str) -> OutpostGeneration:
    return cast(OutpostGeneration, data)
