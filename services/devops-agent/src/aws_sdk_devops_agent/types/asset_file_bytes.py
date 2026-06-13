"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetFileBytes``."""

import base64
from typing import TypeAlias

"""<p>Binary file content</p>"""
AssetFileBytes: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AssetFileBytes) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AssetFileBytes:
    return base64.b64decode(data)
