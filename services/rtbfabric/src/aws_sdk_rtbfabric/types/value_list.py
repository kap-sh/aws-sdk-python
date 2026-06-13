"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ValueList``."""

from typing import TypeAlias

ValueList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ValueList:
    return list(data)
