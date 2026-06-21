"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationPillar``."""

from typing import Literal, TypeAlias, cast

RecommendationPillar: TypeAlias = Literal[
    "cost_optimizing",
    "performance",
    "security",
    "service_limits",
    "fault_tolerance",
    "operational_excellence",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationPillar) -> str:
    return value


def deserialize_json(data: str) -> RecommendationPillar:
    return cast(RecommendationPillar, data)
