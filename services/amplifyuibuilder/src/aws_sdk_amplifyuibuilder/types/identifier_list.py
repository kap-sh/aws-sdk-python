"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#IdentifierList``."""

from typing import TypeAlias

IdentifierList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: IdentifierList) -> list:
    return list(value)


def deserialize_json(data: list) -> IdentifierList:
    return list(data)
