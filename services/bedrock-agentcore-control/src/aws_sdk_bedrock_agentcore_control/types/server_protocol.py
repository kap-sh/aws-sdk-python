"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ServerProtocol``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

ServerProtocol: TypeAlias = Literal[
    "MCP",
    "HTTP",
    "A2A",
    "AGUI",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MCP",
        "HTTP",
        "A2A",
        "AGUI",
    )
)


def serialize_json(value: ServerProtocol) -> str:
    return value


def deserialize_json(data: str) -> ServerProtocol:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServerProtocol value: {data!r}")
    return cast(ServerProtocol, data)
