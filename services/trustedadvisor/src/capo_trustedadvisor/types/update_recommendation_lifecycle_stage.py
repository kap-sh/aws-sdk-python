"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#UpdateRecommendationLifecycleStage``."""

from typing import Literal, TypeAlias, cast

UpdateRecommendationLifecycleStage: TypeAlias = Literal[
    "pending_response",
    "in_progress",
    "dismissed",
    "resolved",
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommendationLifecycleStage) -> str:
    return value


def deserialize_json(data: str) -> UpdateRecommendationLifecycleStage:
    return cast(UpdateRecommendationLifecycleStage, data)
