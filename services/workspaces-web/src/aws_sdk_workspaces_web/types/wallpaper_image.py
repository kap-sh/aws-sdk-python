"""Generated from Smithy shape ``com.amazonaws.workspacesweb#WallpaperImage``."""

import base64
from typing import TypeAlias

WallpaperImage: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: WallpaperImage) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> WallpaperImage:
    return base64.b64decode(data)
