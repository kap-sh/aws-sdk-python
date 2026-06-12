"""Generated from Smithy shape ``com.amazonaws.panorama#Certificates``."""

import base64
from typing import TypeAlias

Certificates: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: Certificates) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> Certificates:
    return base64.b64decode(data)
