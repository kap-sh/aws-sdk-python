"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#RegionList``."""

from typing import TypeAlias

RegionList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: RegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> RegionList:
    return list(data)
