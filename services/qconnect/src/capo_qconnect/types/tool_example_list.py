"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolExampleList``."""

from typing import TypeAlias

ToolExampleList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ToolExampleList) -> list:
    return list(value)


def deserialize_json(data: list) -> ToolExampleList:
    return list(data)
