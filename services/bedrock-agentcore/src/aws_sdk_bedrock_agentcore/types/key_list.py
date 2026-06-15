"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#KeyList``."""

from typing import TypeAlias

KeyList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: KeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> KeyList:
    return list(data)
