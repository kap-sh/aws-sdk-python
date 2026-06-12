"""Generated from Smithy shape ``com.amazonaws.iotwireless#GeoJsonPayload``."""

import base64
from typing import TypeAlias

GeoJsonPayload: TypeAlias = bytes


# --- restJson1 ser/de ---
def serialize_json(value: GeoJsonPayload) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_json(data: str) -> GeoJsonPayload:
    return base64.b64decode(data)
