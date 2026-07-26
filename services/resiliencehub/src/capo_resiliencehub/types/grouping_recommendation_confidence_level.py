"""Generated from Smithy shape ``com.amazonaws.resiliencehub#GroupingRecommendationConfidenceLevel``."""

from typing import Literal, TypeAlias, cast

GroupingRecommendationConfidenceLevel: TypeAlias = Literal[
    "High",
    "Medium",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingRecommendationConfidenceLevel) -> str:
    return value


def deserialize_json(data: str) -> GroupingRecommendationConfidenceLevel:
    return cast(GroupingRecommendationConfidenceLevel, data)
