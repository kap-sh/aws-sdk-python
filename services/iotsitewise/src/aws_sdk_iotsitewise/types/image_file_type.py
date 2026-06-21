"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ImageFileType``."""

from typing import Literal, TypeAlias, cast

ImageFileType: TypeAlias = Literal["PNG",]


# --- restJson1 ser/de ---
def serialize_json(value: ImageFileType) -> str:
    return value


def deserialize_json(data: str) -> ImageFileType:
    return cast(ImageFileType, data)
