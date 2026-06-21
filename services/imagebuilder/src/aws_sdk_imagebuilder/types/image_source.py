"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageSource``."""

from typing import Literal, TypeAlias, cast

ImageSource: TypeAlias = Literal[
    "AMAZON_MANAGED",
    "AWS_MARKETPLACE",
    "IMPORTED",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageSource) -> str:
    return value


def deserialize_json(data: str) -> ImageSource:
    return cast(ImageSource, data)
