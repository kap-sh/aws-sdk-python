"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RenderRecommendationType``."""

from typing import Literal, TypeAlias, cast

RenderRecommendationType: TypeAlias = Literal[
    "Alarm",
    "Sop",
    "Test",
]


# --- restJson1 ser/de ---
def serialize_json(value: RenderRecommendationType) -> str:
    return value


def deserialize_json(data: str) -> RenderRecommendationType:
    return cast(RenderRecommendationType, data)
