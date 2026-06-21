"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudWordCasing``."""

from typing import Literal, TypeAlias, cast

WordCloudWordCasing: TypeAlias = Literal[
    "LOWER_CASE",
    "EXISTING_CASE",
]


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudWordCasing) -> str:
    return value


def deserialize_json(data: str) -> WordCloudWordCasing:
    return cast(WordCloudWordCasing, data)
