"""Generated from Smithy shape ``com.amazonaws.quicksight#TableFieldOrderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.field_id

TableFieldOrderList: TypeAlias = list["capo_quicksight.types.field_id.FieldId"]


# --- restJson1 ser/de ---
def serialize_json(value: TableFieldOrderList) -> list:
    return list(value)


def deserialize_json(data: list) -> TableFieldOrderList:
    return list(data)
