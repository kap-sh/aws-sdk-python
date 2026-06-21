"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ImageInputFormat``."""

from typing import Literal, TypeAlias, cast

ImageInputFormat: TypeAlias = Literal[
    "png",
    "jpeg",
    "gif",
    "webp",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageInputFormat) -> str:
    return value


def deserialize_json(data: str) -> ImageInputFormat:
    return cast(ImageInputFormat, data)
