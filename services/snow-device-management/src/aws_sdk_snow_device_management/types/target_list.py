"""Generated from Smithy shape ``com.amazonaws.snowdevicemanagement#TargetList``."""

from typing import TypeAlias

TargetList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: TargetList) -> list:
    return list(value)


def deserialize_json(data: list) -> TargetList:
    return list(data)
