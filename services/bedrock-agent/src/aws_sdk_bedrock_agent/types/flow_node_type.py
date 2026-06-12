"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent.errors import DeserializationError

FlowNodeType: TypeAlias = Literal[
    "Input",
    "Output",
    "KnowledgeBase",
    "Condition",
    "Lex",
    "Prompt",
    "LambdaFunction",
    "Storage",
    "Agent",
    "Retrieval",
    "Iterator",
    "Collector",
    "InlineCode",
    "Loop",
    "LoopInput",
    "LoopController",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Input",
        "Output",
        "KnowledgeBase",
        "Condition",
        "Lex",
        "Prompt",
        "LambdaFunction",
        "Storage",
        "Agent",
        "Retrieval",
        "Iterator",
        "Collector",
        "InlineCode",
        "Loop",
        "LoopInput",
        "LoopController",
    )
)


def serialize_json(value: FlowNodeType) -> str:
    return value


def deserialize_json(data: str) -> FlowNodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowNodeType value: {data!r}")
    return cast(FlowNodeType, data)
