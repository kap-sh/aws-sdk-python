"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

ToolName: TypeAlias = Literal[
    "executeCode",
    "executeCommand",
    "readFiles",
    "listFiles",
    "removeFiles",
    "writeFiles",
    "startCommandExecution",
    "getTask",
    "stopTask",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "executeCode",
        "executeCommand",
        "readFiles",
        "listFiles",
        "removeFiles",
        "writeFiles",
        "startCommandExecution",
        "getTask",
        "stopTask",
    )
)


def serialize_json(value: ToolName) -> str:
    return value


def deserialize_json(data: str) -> ToolName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ToolName value: {data!r}")
    return cast(ToolName, data)
