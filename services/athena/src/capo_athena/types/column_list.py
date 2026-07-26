"""Generated from Smithy shape ``com.amazonaws.athena#ColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.column

ColumnList: TypeAlias = list["capo_athena.types.column.Column"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnList) -> list:
    import capo_athena.types.column

    out: list = []
    for item in value:
        out.append(capo_athena.types.column.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ColumnList:
    import capo_athena.types.column

    out: ColumnList = []
    for item in data:
        out.append(capo_athena.types.column.deserialize_aws_json_1_1(item))
    return out
