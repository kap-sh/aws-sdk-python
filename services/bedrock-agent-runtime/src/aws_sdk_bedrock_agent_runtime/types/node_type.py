"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: NodeType) -> str:
    return value


def deserialize_json(data: str) -> NodeType:
    return cast(NodeType, data)
