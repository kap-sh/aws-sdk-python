"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WhatsAppMessageBlob``."""

import base64
from typing import TypeAlias

WhatsAppMessageBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: WhatsAppMessageBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> WhatsAppMessageBlob:
    return base64.b64decode(data)
