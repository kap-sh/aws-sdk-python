"""Generated from Smithy shape ``com.amazonaws.iotdataplane#UserPropertiesBlob``."""

import base64
from typing import TypeAlias

UserPropertiesBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: UserPropertiesBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> UserPropertiesBlob:
    return base64.b64decode(data)
