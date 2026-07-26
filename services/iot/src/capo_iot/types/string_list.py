"""Generated from Smithy shape ``com.amazonaws.iot#StringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.string_value

StringList: TypeAlias = list["capo_iot.types.string_value.stringValue"]


# --- restJson1 ser/de ---
def serialize_json(value: StringList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringList:
    return list(data)
