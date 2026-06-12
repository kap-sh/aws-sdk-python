"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ResourceArnsList``."""

from typing import TypeAlias

ResourceArnsList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceArnsList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceArnsList:
    return list(data)
