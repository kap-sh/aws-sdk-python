"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#ColumnNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.column_name

ColumnNamesList: TypeAlias = list[
    "aws_sdk_personalize_runtime.types.column_name.ColumnName"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnNamesList) -> list:
    return list(value)


def deserialize_json(data: list) -> ColumnNamesList:
    return list(data)
