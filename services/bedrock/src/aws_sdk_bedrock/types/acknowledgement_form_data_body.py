"""Generated from Smithy shape ``com.amazonaws.bedrock#AcknowledgementFormDataBody``."""

import base64
from typing import TypeAlias

AcknowledgementFormDataBody: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: AcknowledgementFormDataBody) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> AcknowledgementFormDataBody:
    return base64.b64decode(data)
