"""Generated from Smithy shape ``com.amazonaws.connect#FlowModuleType``."""

from typing import Literal, TypeAlias, cast

FlowModuleType: TypeAlias = Literal["MCP",]


# --- restJson1 ser/de ---
def serialize_json(value: FlowModuleType) -> str:
    return value


def deserialize_json(data: str) -> FlowModuleType:
    return cast(FlowModuleType, data)
