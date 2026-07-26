"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#InferenceResponseBody``."""

import base64
from typing import TypeAlias

"""Sensitive binary payload containing model inference response data."""
InferenceResponseBody: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: InferenceResponseBody) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> InferenceResponseBody:
    return base64.b64decode(data)
