"""Generated from Smithy shape ``com.amazonaws.wisdom#RecommendationIdList``."""

from typing import TypeAlias

RecommendationIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> RecommendationIdList:
    return list(data)
