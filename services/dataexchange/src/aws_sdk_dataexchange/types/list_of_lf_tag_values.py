"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfLFTagValues``."""

from typing import TypeAlias

ListOfLFTagValues: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfLFTagValues) -> list:
    return list(value)


def deserialize_json(data: list) -> ListOfLFTagValues:
    return list(data)
