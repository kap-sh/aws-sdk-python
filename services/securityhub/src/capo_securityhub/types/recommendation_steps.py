"""Generated from Smithy shape ``com.amazonaws.securityhub#RecommendationSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.recommendation_step

RecommendationSteps: TypeAlias = list[
    "capo_securityhub.types.recommendation_step.RecommendationStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationSteps) -> list:
    import capo_securityhub.types.recommendation_step

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.recommendation_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecommendationSteps:
    import capo_securityhub.types.recommendation_step

    out: RecommendationSteps = []
    for item in data:
        out.append(capo_securityhub.types.recommendation_step.deserialize_json(item))
    return out
