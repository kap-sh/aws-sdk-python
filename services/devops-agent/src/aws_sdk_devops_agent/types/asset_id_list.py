"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssetIdList``."""

from typing import TypeAlias

AssetIdList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AssetIdList:
    return list(data)
