"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#RecommendationIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.recommendation_id

RecommendationIds: TypeAlias = list[
    "capo_codeguru_reviewer.types.recommendation_id.RecommendationId"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationIds) -> list:
    return list(value)


def deserialize_json(data: list) -> RecommendationIds:
    return list(data)
