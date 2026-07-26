"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ManagedViewArnList``."""

from typing import TypeAlias

ManagedViewArnList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedViewArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ManagedViewArnList:
    return list(data)
