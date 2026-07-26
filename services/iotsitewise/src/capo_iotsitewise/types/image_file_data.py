"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ImageFileData``."""

import base64
from typing import TypeAlias

ImageFileData: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: ImageFileData) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> ImageFileData:
    return base64.b64decode(data)
