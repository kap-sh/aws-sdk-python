"""Generated from Smithy shape ``com.amazonaws.resiliencehub#GroupingRecommendationRejectionReason``."""

from typing import Literal, TypeAlias, cast

GroupingRecommendationRejectionReason: TypeAlias = Literal[
    "DistinctBusinessPurpose",
    "SeparateDataConcern",
    "DistinctUserGroupHandling",
    "Other",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingRecommendationRejectionReason) -> str:
    return value


def deserialize_json(data: str) -> GroupingRecommendationRejectionReason:
    return cast(GroupingRecommendationRejectionReason, data)
