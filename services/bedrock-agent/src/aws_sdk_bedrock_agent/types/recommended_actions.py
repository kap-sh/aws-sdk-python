"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RecommendedActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.recommended_action

RecommendedActions: TypeAlias = list[
    "aws_sdk_bedrock_agent.types.recommended_action.RecommendedAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendedActions) -> list:
    return list(value)


def deserialize_json(data: list) -> RecommendedActions:
    return list(data)
