"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EvaluationToolNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.evaluation_tool_name

EvaluationToolNames: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.evaluation_tool_name.EvaluationToolName"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationToolNames) -> list:
    return list(value)


def deserialize_json(data: list) -> EvaluationToolNames:
    return list(data)
