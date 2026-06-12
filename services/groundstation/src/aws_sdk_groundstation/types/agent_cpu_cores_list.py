"""Generated from Smithy shape ``com.amazonaws.groundstation#AgentCpuCoresList``."""

from typing import TypeAlias

AgentCpuCoresList: TypeAlias = list["int"]


# --- restJson1 ser/de ---
def serialize_json(value: AgentCpuCoresList) -> list:
    return list(value)


def deserialize_json(data: list) -> AgentCpuCoresList:
    return list(data)