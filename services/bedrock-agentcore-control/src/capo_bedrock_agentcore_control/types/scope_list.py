"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ScopeList``."""

from typing import TypeAlias

ScopeList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ScopeList:
    return list(data)
