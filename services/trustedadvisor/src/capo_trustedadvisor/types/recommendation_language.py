"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationLanguage``."""

from typing import Literal, TypeAlias, cast

RecommendationLanguage: TypeAlias = Literal[
    "en",
    "ja",
    "zh",
    "fr",
    "de",
    "ko",
    "zh_TW",
    "it",
    "es",
    "pt_BR",
    "id",
]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationLanguage) -> str:
    return value


def deserialize_json(data: str) -> RecommendationLanguage:
    return cast(RecommendationLanguage, data)
