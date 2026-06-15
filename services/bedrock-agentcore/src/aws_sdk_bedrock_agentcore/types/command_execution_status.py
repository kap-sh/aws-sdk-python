"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CommandExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

CommandExecutionStatus: TypeAlias = Literal[
    "COMPLETED",
    "TIMED_OUT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "TIMED_OUT",
    )
)


def serialize_json(value: CommandExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> CommandExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommandExecutionStatus value: {data!r}")
    return cast(CommandExecutionStatus, data)
