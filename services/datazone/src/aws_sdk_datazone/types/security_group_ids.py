"""Generated from Smithy shape ``com.amazonaws.datazone#SecurityGroupIds``."""

from typing import TypeAlias

SecurityGroupIds: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupIds:
    return list(data)
