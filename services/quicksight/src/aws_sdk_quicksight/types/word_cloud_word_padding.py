"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudWordPadding``."""

from typing import Literal, TypeAlias, cast

WordCloudWordPadding: TypeAlias = Literal[
    "NONE",
    "SMALL",
    "MEDIUM",
    "LARGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudWordPadding) -> str:
    return value


def deserialize_json(data: str) -> WordCloudWordPadding:
    return cast(WordCloudWordPadding, data)
