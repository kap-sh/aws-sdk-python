"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolName``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ToolName) -> str:
    return value


def deserialize_json(data: str) -> ToolName:
    return cast(ToolName, data)
