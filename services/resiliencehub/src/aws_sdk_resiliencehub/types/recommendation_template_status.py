"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationTemplateStatus``."""

from typing import Literal, TypeAlias, cast

RecommendationTemplateStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Failed",
    "Success",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTemplateStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommendationTemplateStatus:
    return cast(RecommendationTemplateStatus, data)
