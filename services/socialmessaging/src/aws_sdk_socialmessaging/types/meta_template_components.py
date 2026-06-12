"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaTemplateComponents``."""

import base64
from typing import TypeAlias

MetaTemplateComponents: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: MetaTemplateComponents) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> MetaTemplateComponents:
    return base64.b64decode(data)
