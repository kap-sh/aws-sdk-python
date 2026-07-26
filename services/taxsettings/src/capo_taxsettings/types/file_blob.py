"""Generated from Smithy shape ``com.amazonaws.taxsettings#FileBlob``."""

import base64
from typing import TypeAlias

FileBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: FileBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> FileBlob:
    return base64.b64decode(data)
