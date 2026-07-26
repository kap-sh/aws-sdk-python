"""Generated from Smithy shape ``com.amazonaws.backupsearch#ResourceArnList``."""

from typing import TypeAlias

ResourceArnList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceArnList:
    return list(data)
