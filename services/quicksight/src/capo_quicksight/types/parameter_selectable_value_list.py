"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterSelectableValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.string

ParameterSelectableValueList: TypeAlias = list["capo_quicksight.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterSelectableValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> ParameterSelectableValueList:
    return list(data)
