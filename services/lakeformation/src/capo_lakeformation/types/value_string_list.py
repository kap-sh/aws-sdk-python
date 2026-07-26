"""Generated from Smithy shape ``com.amazonaws.lakeformation#ValueStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.value_string

ValueStringList: TypeAlias = list["capo_lakeformation.types.value_string.ValueString"]


# --- restJson1 ser/de ---
def serialize_json(value: ValueStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> ValueStringList:
    return list(data)
