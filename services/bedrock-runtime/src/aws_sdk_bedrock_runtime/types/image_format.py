"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ImageFormat``."""

from typing import Literal, TypeAlias, cast

ImageFormat: TypeAlias = Literal[
    "png",
    "jpeg",
    "gif",
    "webp",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageFormat) -> str:
    return value


def deserialize_json(data: str) -> ImageFormat:
    return cast(ImageFormat, data)
