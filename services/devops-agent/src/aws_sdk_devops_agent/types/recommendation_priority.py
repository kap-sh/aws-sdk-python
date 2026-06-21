"""Generated from Smithy shape ``com.amazonaws.devopsagent#RecommendationPriority``."""

from typing import Literal, TypeAlias, cast

"""<p>Priority level of a recommendation</p>"""
RecommendationPriority: TypeAlias = Literal[
    "HIGH",
    "MEDIUM",
    "LOW",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationPriority) -> str:
    return value


def deserialize_json(data: str) -> RecommendationPriority:
    return cast(RecommendationPriority, data)
