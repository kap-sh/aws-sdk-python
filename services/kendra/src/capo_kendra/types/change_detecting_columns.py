"""Generated from Smithy shape ``com.amazonaws.kendra#ChangeDetectingColumns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.column_name

ChangeDetectingColumns: TypeAlias = list["capo_kendra.types.column_name.ColumnName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChangeDetectingColumns) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ChangeDetectingColumns:
    return list(data)
