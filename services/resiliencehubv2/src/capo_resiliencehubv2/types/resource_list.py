"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResourceList``."""

from typing import TypeAlias

ResourceList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceList:
    return list(data)
