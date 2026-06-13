"""Generated from Smithy shape ``com.amazonaws.quicksight#RenameColumnOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.rename_column_operation

RenameColumnOperationList: TypeAlias = list[
    "aws_sdk_quicksight.types.rename_column_operation.RenameColumnOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: RenameColumnOperationList) -> list:
    import aws_sdk_quicksight.types.rename_column_operation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.rename_column_operation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RenameColumnOperationList:
    import aws_sdk_quicksight.types.rename_column_operation

    out: RenameColumnOperationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.rename_column_operation.deserialize_json(item)
        )
    return out
