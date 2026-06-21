"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageExtractionStatus``."""

from typing import Literal, TypeAlias, cast

ImageExtractionStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageExtractionStatus) -> str:
    return value


def deserialize_json(data: str) -> ImageExtractionStatus:
    return cast(ImageExtractionStatus, data)
