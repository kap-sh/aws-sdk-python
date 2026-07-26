"""Generated from Smithy shape ``com.amazonaws.iot#CommandExecutionStatus``."""

from typing import Literal, TypeAlias, cast

CommandExecutionStatus: TypeAlias = Literal[
    "CREATED",
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
    "REJECTED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: CommandExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> CommandExecutionStatus:
    return cast(CommandExecutionStatus, data)
