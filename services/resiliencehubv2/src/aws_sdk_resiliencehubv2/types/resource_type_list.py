"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ResourceTypeList``."""

from typing import TypeAlias

ResourceTypeList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceTypeList:
    return list(data)
