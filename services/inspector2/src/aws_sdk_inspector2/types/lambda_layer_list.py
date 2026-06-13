"""Generated from Smithy shape ``com.amazonaws.inspector2#LambdaLayerList``."""

from typing import TypeAlias

LambdaLayerList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: LambdaLayerList) -> list:
    return list(value)


def deserialize_json(data: list) -> LambdaLayerList:
    return list(data)
