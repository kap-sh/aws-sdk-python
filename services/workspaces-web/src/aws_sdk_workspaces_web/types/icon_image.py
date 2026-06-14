"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IconImage``."""

import base64
from typing import TypeAlias

IconImage: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: IconImage) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> IconImage:
    return base64.b64decode(data)
