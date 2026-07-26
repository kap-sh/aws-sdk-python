"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SecurityGroupIdList``."""

from typing import TypeAlias

SecurityGroupIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupIdList:
    return list(data)
