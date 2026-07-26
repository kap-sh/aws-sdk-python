"""Generated from Smithy shape ``com.amazonaws.omics#ArnList``."""

from typing import TypeAlias

ArnList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ArnList:
    return list(data)
