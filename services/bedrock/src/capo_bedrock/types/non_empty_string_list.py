"""Generated from Smithy shape ``com.amazonaws.bedrock#NonEmptyStringList``."""

from typing import TypeAlias

NonEmptyStringList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: NonEmptyStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> NonEmptyStringList:
    return [item for item in data if item is not None]
