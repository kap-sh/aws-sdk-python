"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#StringList``."""

from typing import TypeAlias

StringList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: StringList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringList:
    return list(data)
