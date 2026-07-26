"""Generated from Smithy shape ``com.amazonaws.quicksight#RenameColumnOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.rename_column_operation

RenameColumnOperationList: TypeAlias = list[
    "capo_quicksight.types.rename_column_operation.RenameColumnOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: RenameColumnOperationList) -> list:
    import capo_quicksight.types.rename_column_operation

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.rename_column_operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> RenameColumnOperationList:
    import capo_quicksight.types.rename_column_operation

    out: RenameColumnOperationList = []
    for item in data:
        out.append(capo_quicksight.types.rename_column_operation.deserialize_json(item))
    return out
