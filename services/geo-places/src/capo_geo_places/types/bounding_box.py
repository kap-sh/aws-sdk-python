"""Generated from Smithy shape ``com.amazonaws.geoplaces#BoundingBox``."""

from typing import TypeAlias

BoundingBox: TypeAlias = list["float"]


# --- restJson1 ser/de ---
def serialize_json(value: BoundingBox) -> list:
    return list(value)


def deserialize_json(data: list) -> BoundingBox:
    return list(data)
