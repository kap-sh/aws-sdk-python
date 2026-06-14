"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Body``."""

import base64
from typing import TypeAlias

Body: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: Body) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> Body:
    return base64.b64decode(data)
