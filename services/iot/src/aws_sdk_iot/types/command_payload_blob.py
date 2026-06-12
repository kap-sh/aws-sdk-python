"""Generated from Smithy shape ``com.amazonaws.iot#CommandPayloadBlob``."""

import base64
from typing import TypeAlias

CommandPayloadBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: CommandPayloadBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> CommandPayloadBlob:
    return base64.b64decode(data)
