"""Generated from Smithy shape ``com.amazonaws.securityagent#TaskIdList``."""

from typing import TypeAlias

TaskIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: TaskIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> TaskIdList:
    return list(data)
