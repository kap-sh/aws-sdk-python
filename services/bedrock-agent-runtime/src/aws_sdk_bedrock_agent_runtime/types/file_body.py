"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FileBody``."""

import base64
from typing import TypeAlias

FileBody: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: FileBody) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> FileBody:
    return base64.b64decode(data)
