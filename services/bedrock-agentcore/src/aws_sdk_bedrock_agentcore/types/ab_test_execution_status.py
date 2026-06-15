"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ABTestExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

ABTestExecutionStatus: TypeAlias = Literal[
    "PAUSED",
    "RUNNING",
    "STOPPED",
    "NOT_STARTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PAUSED",
        "RUNNING",
        "STOPPED",
        "NOT_STARTED",
    )
)


def serialize_json(value: ABTestExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> ABTestExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ABTestExecutionStatus value: {data!r}")
    return cast(ABTestExecutionStatus, data)
