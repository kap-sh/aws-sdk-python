"""Generated from Smithy shape ``com.amazonaws.neptunedata#EdgeProperties``."""

from typing import TypeAlias

EdgeProperties: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: EdgeProperties) -> list:
    return list(value)


def deserialize_json(data: list) -> EdgeProperties:
    return list(data)