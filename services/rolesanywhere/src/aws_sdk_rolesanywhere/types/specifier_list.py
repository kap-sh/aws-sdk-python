"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#SpecifierList``."""

from typing import TypeAlias

SpecifierList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: SpecifierList) -> list:
    return list(value)


def deserialize_json(data: list) -> SpecifierList:
    return list(data)
