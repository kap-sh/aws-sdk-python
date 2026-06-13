"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldOrderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.field_id

FieldOrderList: TypeAlias = list["aws_sdk_quicksight.types.field_id.FieldId"]


# --- restJson1 ser/de ---
def serialize_json(value: FieldOrderList) -> list:
    return list(value)


def deserialize_json(data: list) -> FieldOrderList:
    return list(data)
