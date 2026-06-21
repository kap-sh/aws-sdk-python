"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudWordScaling``."""

from typing import Literal, TypeAlias, cast

WordCloudWordScaling: TypeAlias = Literal[
    "EMPHASIZE",
    "NORMAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudWordScaling) -> str:
    return value


def deserialize_json(data: str) -> WordCloudWordScaling:
    return cast(WordCloudWordScaling, data)
