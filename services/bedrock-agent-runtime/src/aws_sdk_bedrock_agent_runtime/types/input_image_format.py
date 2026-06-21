"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InputImageFormat``."""

from typing import Literal, TypeAlias, cast

InputImageFormat: TypeAlias = Literal[
    "png",
    "jpeg",
    "gif",
    "webp",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputImageFormat) -> str:
    return value


def deserialize_json(data: str) -> InputImageFormat:
    return cast(InputImageFormat, data)
