"""Generated from Smithy shape ``com.amazonaws.groundstation#SubnetList``."""

from typing import TypeAlias

SubnetList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: SubnetList) -> list:
    return list(value)


def deserialize_json(data: list) -> SubnetList:
    return list(data)
