"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudWordOrientation``."""

from typing import Literal, TypeAlias, cast

WordCloudWordOrientation: TypeAlias = Literal[
    "HORIZONTAL",
    "HORIZONTAL_AND_VERTICAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudWordOrientation) -> str:
    return value


def deserialize_json(data: str) -> WordCloudWordOrientation:
    return cast(WordCloudWordOrientation, data)
