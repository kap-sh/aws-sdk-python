"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaTemplateDefinition``."""

import base64
from typing import TypeAlias

MetaTemplateDefinition: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: MetaTemplateDefinition) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> MetaTemplateDefinition:
    return base64.b64decode(data)
