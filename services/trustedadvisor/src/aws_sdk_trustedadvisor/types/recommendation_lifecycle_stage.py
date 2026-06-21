"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationLifecycleStage``."""

from typing import Literal, TypeAlias, cast

RecommendationLifecycleStage: TypeAlias = Literal[
    "in_progress",
    "pending_response",
    "dismissed",
    "resolved",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationLifecycleStage) -> str:
    return value


def deserialize_json(data: str) -> RecommendationLifecycleStage:
    return cast(RecommendationLifecycleStage, data)
