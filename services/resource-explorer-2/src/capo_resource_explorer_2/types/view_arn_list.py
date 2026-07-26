"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ViewArnList``."""

from typing import TypeAlias

ViewArnList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ViewArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ViewArnList:
    return list(data)
