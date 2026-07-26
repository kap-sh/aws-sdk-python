"""Generated from Smithy shape ``com.amazonaws.inspector2#TagList``."""

from typing import TypeAlias

TagList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: TagList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagList:
    return list(data)
