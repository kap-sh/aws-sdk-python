"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ServerProtocol``."""

from typing import Literal, TypeAlias, cast

ServerProtocol: TypeAlias = Literal[
    "MCP",
    "HTTP",
    "A2A",
    "AGUI",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServerProtocol) -> str:
    return value


def deserialize_json(data: str) -> ServerProtocol:
    return cast(ServerProtocol, data)
