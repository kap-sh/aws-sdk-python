"""Generated from Smithy shape ``com.amazonaws.qapps#MemoryReferenceList``."""

from typing import TypeAlias

MemoryReferenceList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: MemoryReferenceList) -> list:
    return list(value)


def deserialize_json(data: list) -> MemoryReferenceList:
    return list(data)
