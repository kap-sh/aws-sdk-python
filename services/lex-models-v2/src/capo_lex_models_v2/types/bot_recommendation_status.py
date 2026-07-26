"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotRecommendationStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: BotRecommendationStatus) -> str:
    return value


def deserialize_json(data: str) -> BotRecommendationStatus:
    return cast(BotRecommendationStatus, data)
