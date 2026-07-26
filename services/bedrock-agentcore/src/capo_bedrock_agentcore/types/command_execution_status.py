"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CommandExecutionStatus``."""

from typing import Literal, TypeAlias, cast

CommandExecutionStatus: TypeAlias = Literal[
    "COMPLETED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: CommandExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> CommandExecutionStatus:
    return cast(CommandExecutionStatus, data)
