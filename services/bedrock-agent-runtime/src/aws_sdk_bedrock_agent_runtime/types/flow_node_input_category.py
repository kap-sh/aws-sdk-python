"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowNodeInputCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

FlowNodeInputCategory: TypeAlias = Literal[
    "LoopCondition",
    "ReturnValueToLoopStart",
    "ExitLoop",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LoopCondition",
        "ReturnValueToLoopStart",
        "ExitLoop",
    )
)


def serialize_json(value: FlowNodeInputCategory) -> str:
    return value


def deserialize_json(data: str) -> FlowNodeInputCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowNodeInputCategory value: {data!r}")
    return cast(FlowNodeInputCategory, data)
