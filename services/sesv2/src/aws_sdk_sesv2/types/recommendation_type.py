"""Generated from Smithy shape ``com.amazonaws.sesv2#RecommendationType``."""

from typing import Literal, TypeAlias, cast

RecommendationType: TypeAlias = Literal[
    "DKIM",
    "DMARC",
    "SPF",
    "BIMI",
    "COMPLAINT",
    "BOUNCE",
    "FEEDBACK_3P",
    "IP_LISTING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationType) -> str:
    return value


def deserialize_json(data: str) -> RecommendationType:
    return cast(RecommendationType, data)
