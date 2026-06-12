"""Generated from Smithy shape ``com.amazonaws.personalize#ColumnNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.column_name

ColumnNamesList: TypeAlias = list["aws_sdk_personalize.types.column_name.ColumnName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnNamesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ColumnNamesList:
    return list(data)
