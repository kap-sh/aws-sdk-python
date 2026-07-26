"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ServiceViewArnList``."""

from typing import TypeAlias

ServiceViewArnList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceViewArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ServiceViewArnList:
    return list(data)
