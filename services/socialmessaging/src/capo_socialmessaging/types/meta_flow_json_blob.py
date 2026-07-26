"""Generated from Smithy shape ``com.amazonaws.socialmessaging#MetaFlowJsonBlob``."""

import base64
from typing import TypeAlias

MetaFlowJsonBlob: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: MetaFlowJsonBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> MetaFlowJsonBlob:
    return base64.b64decode(data)
