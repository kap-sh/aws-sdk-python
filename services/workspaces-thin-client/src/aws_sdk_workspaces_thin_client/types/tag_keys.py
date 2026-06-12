"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#TagKeys``."""

from typing import TypeAlias

TagKeys: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeys:
    return list(data)
