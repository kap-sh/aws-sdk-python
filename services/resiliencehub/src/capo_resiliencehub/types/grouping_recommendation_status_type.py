"""Generated from Smithy shape ``com.amazonaws.resiliencehub#GroupingRecommendationStatusType``."""

from typing import Literal, TypeAlias, cast

GroupingRecommendationStatusType: TypeAlias = Literal[
    "Accepted",
    "Rejected",
    "PendingDecision",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingRecommendationStatusType) -> str:
    return value


def deserialize_json(data: str) -> GroupingRecommendationStatusType:
    return cast(GroupingRecommendationStatusType, data)
