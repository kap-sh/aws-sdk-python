"""Generated from Smithy shape ``com.amazonaws.notifications#Tags``."""

from typing import TypeAlias

Tags: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: Tags) -> list:
    return list(value)


def deserialize_json(data: list) -> Tags:
    return list(data)
