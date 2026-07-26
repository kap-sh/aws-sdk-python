"""Generated from Smithy shape ``com.amazonaws.lakeformation#StringValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.string_value

StringValueList: TypeAlias = list["capo_lakeformation.types.string_value.StringValue"]


# --- restJson1 ser/de ---
def serialize_json(value: StringValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringValueList:
    return list(data)
