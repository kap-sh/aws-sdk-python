"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MatchPathPatterns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.match_path_pattern

MatchPathPatterns: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.match_path_pattern.MatchPathPattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchPathPatterns) -> list:
    return list(value)


def deserialize_json(data: list) -> MatchPathPatterns:
    return [item for item in data if item is not None]
