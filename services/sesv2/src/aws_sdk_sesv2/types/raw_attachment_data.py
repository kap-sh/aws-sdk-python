"""Generated from Smithy shape ``com.amazonaws.sesv2#RawAttachmentData``."""

import base64
from typing import TypeAlias

RawAttachmentData: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: RawAttachmentData) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> RawAttachmentData:
    return base64.b64decode(data)
