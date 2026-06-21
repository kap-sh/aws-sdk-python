"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationType``."""

from typing import Literal, TypeAlias, cast

RecommendationType: TypeAlias = Literal[
    "standard",
    "priority",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationType) -> str:
    return value


def deserialize_json(data: str) -> RecommendationType:
    return cast(RecommendationType, data)
