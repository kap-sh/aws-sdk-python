"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of recommendation to generate.</p>"""
RecommendationType: TypeAlias = Literal[
    "SYSTEM_PROMPT_RECOMMENDATION",
    "TOOL_DESCRIPTION_RECOMMENDATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationType) -> str:
    return value


def deserialize_json(data: str) -> RecommendationType:
    return cast(RecommendationType, data)
