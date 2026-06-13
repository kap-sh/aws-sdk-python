"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPToolsList``."""

from typing import TypeAlias

MCPToolsList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: MCPToolsList) -> list:
    return list(value)


def deserialize_json(data: list) -> MCPToolsList:
    return list(data)
