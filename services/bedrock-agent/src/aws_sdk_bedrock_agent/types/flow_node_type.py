"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowNodeType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: FlowNodeType) -> str:
    return value


def deserialize_json(data: str) -> FlowNodeType:
    return cast(FlowNodeType, data)
