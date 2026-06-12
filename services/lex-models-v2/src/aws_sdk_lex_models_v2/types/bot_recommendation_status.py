"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotRecommendationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

BotRecommendationStatus: TypeAlias = Literal[
    "Processing",
    "Deleting",
    "Deleted",
    "Downloading",
    "Updating",
    "Available",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Processing",
        "Deleting",
        "Deleted",
        "Downloading",
        "Updating",
        "Available",
        "Failed",
        "Stopping",
        "Stopped",
    )
)


def serialize_json(value: BotRecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> BotRecommendationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BotRecommendationStatus value: {data!r}")
    return cast(BotRecommendationStatus, data)
