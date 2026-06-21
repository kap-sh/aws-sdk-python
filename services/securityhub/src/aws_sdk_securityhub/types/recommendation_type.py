"""Generated from Smithy shape ``com.amazonaws.securityhub#RecommendationType``."""

from typing import Literal, TypeAlias, cast

RecommendationType: TypeAlias = Literal["UNUSED_PERMISSION_RECOMMENDATION",]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationType) -> str:
    return value


def deserialize_json(data: str) -> RecommendationType:
    return cast(RecommendationType, data)
