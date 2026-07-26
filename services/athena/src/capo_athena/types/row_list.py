"""Generated from Smithy shape ``com.amazonaws.athena#RowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.row

RowList: TypeAlias = list["capo_athena.types.row.Row"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RowList) -> list:
    import capo_athena.types.row

    out: list = []
    for item in value:
        out.append(capo_athena.types.row.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RowList:
    import capo_athena.types.row

    out: RowList = []
    for item in data:
        out.append(capo_athena.types.row.deserialize_aws_json_1_1(item))
    return out
