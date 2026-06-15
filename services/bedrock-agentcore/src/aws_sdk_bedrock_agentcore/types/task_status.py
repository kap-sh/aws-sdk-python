"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

TaskStatus: TypeAlias = Literal[
    "submitted",
    "working",
    "completed",
    "canceled",
    "failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "submitted",
        "working",
        "completed",
        "canceled",
        "failed",
    )
)


def serialize_json(value: TaskStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskStatus value: {data!r}")
    return cast(TaskStatus, data)
