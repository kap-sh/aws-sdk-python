"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationComplianceStatus``."""

from typing import Literal, TypeAlias, cast

RecommendationComplianceStatus: TypeAlias = Literal[
    "BreachedUnattainable",
    "BreachedCanMeet",
    "MetCanImprove",
    "MissingPolicy",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationComplianceStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationComplianceStatus:
    return cast(RecommendationComplianceStatus, data)
