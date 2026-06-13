"""Generated from Smithy shape ``com.amazonaws.s3tables#IntegerList``."""

from typing import TypeAlias

IntegerList: TypeAlias = list["int"]


# --- restJson1 ser/de ---
def serialize_json(value: IntegerList) -> list:
    return list(value)


def deserialize_json(data: list) -> IntegerList:
    return list(data)
