"""Generated from Smithy shape ``com.amazonaws.bedrockagent#RecommendedActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.recommended_action

RecommendedActions: TypeAlias = list[
    "capo_bedrock_agent.types.recommended_action.RecommendedAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendedActions) -> list:
    return list(value)


def deserialize_json(data: list) -> RecommendedActions:
    return [item for item in data if item is not None]
