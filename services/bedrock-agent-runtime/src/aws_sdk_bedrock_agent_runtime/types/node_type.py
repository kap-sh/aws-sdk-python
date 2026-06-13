"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

NodeType: TypeAlias = Literal[
    "FlowInputNode",
    "FlowOutputNode",
    "LambdaFunctionNode",
    "KnowledgeBaseNode",
    "PromptNode",
    "ConditionNode",
    "LexNode",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FlowInputNode",
        "FlowOutputNode",
        "LambdaFunctionNode",
        "KnowledgeBaseNode",
        "PromptNode",
        "ConditionNode",
        "LexNode",
    )
)


def serialize_json(value: NodeType) -> str:
    return value


def deserialize_json(data: str) -> NodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NodeType value: {data!r}")
    return cast(NodeType, data)
