"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#Target``."""

from typing import TypeAlias

Target: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: Target) -> list:
    return list(value)


def deserialize_json(data: list) -> Target:
    return list(data)
