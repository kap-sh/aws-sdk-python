"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RequiredProperties``."""

from typing import TypeAlias

RequiredProperties: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: RequiredProperties) -> list:
    return list(value)


def deserialize_json(data: list) -> RequiredProperties:
    return list(data)
