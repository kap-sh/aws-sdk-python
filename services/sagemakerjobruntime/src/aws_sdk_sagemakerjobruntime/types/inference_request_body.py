"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#InferenceRequestBody``."""

import base64
from typing import TypeAlias

"""Sensitive binary payload containing customer inference data."""
InferenceRequestBody: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: InferenceRequestBody) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> InferenceRequestBody:
    return base64.b64decode(data)
