"""Generated from Smithy shape ``com.amazonaws.quicksight#WordCloudCloudLayout``."""

from typing import Literal, TypeAlias, cast

WordCloudCloudLayout: TypeAlias = Literal[
    "FLUID",
    "NORMAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: WordCloudCloudLayout) -> str:
    return value


def deserialize_json(data: str) -> WordCloudCloudLayout:
    return cast(WordCloudCloudLayout, data)
