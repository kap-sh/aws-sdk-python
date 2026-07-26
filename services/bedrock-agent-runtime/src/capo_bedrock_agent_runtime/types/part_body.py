"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PartBody``."""

import base64
from typing import TypeAlias

PartBody: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: PartBody) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> PartBody:
    return base64.b64decode(data)
