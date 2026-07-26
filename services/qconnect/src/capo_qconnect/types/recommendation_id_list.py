"""Generated from Smithy shape ``com.amazonaws.qconnect#RecommendationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.recommendation_id

RecommendationIdList: TypeAlias = list[
    "capo_qconnect.types.recommendation_id.RecommendationId"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> RecommendationIdList:
    return list(data)
