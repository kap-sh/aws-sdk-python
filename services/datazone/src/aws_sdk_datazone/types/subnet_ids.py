"""Generated from Smithy shape ``com.amazonaws.datazone#SubnetIds``."""

from typing import TypeAlias

SubnetIds: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetIds:
    return list(data)
