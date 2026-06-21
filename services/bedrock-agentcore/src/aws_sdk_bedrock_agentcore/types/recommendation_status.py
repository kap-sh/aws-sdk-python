"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The lifecycle status of a recommendation.</p>"""
RecommendationStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationStatus:
    return cast(RecommendationStatus, data)
