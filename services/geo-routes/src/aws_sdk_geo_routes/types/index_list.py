"""Generated from Smithy shape ``com.amazonaws.georoutes#IndexList``."""

from typing import TypeAlias

IndexList: TypeAlias = list["int"]


# --- restJson1 ser/de ---
def serialize_json(value: IndexList) -> list:
    return list(value)


def deserialize_json(data: list) -> IndexList:
    return list(data)
