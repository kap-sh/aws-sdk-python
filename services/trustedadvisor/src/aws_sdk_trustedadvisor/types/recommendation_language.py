"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationLanguage``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_trustedadvisor.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: RecommendationLanguage) -> str:
    return value


def deserialize_json(data: str) -> RecommendationLanguage:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommendationLanguage value: {data!r}")
    return cast(RecommendationLanguage, data)
