"""Generated from Smithy shape ``com.amazonaws.outposts#PowerDrawKva``."""

from typing import Literal, TypeAlias, cast

PowerDrawKva: TypeAlias = Literal[
    "POWER_5_KVA",
    "POWER_10_KVA",
    "POWER_15_KVA",
    "POWER_30_KVA",
]


# --- restJson1 ser/de ---
def serialize_json(value: PowerDrawKva) -> str:
    return value


def deserialize_json(data: str) -> PowerDrawKva:
    return cast(PowerDrawKva, data)
