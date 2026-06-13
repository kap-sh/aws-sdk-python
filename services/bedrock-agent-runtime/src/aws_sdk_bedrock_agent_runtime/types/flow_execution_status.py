"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

FlowExecutionStatus: TypeAlias = Literal[
    "Running",
    "Succeeded",
    "Failed",
    "TimedOut",
    "Aborted",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Running",
        "Succeeded",
        "Failed",
        "TimedOut",
        "Aborted",
    )
)


def serialize_json(value: FlowExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> FlowExecutionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowExecutionStatus value: {data!r}")
    return cast(FlowExecutionStatus, data)
