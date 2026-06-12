"""Generated from Smithy shape ``com.amazonaws.sagemakerjobruntime#DoubleList``."""

from typing import TypeAlias

DoubleList: TypeAlias = list["float"]


# --- restJson1 ser/de ---
def serialize_json(value: DoubleList) -> list:
    return list(value)


def deserialize_json(data: list) -> DoubleList:
    return list(data)
