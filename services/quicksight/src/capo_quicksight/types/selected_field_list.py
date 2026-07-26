"""Generated from Smithy shape ``com.amazonaws.quicksight#SelectedFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.field_id

SelectedFieldList: TypeAlias = list["capo_quicksight.types.field_id.FieldId"]


# --- restJson1 ser/de ---
def serialize_json(value: SelectedFieldList) -> list:
    return list(value)


def deserialize_json(data: list) -> SelectedFieldList:
    return list(data)
