"""Generated from Smithy shape ``com.amazonaws.kendra#TableRowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.table_row

TableRowList: TypeAlias = list["aws_sdk_kendra.types.table_row.TableRow"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableRowList) -> list:
    import aws_sdk_kendra.types.table_row

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.table_row.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TableRowList:
    import aws_sdk_kendra.types.table_row

    out: TableRowList = []
    for item in data:
        out.append(aws_sdk_kendra.types.table_row.deserialize_aws_json_1_1(item))
    return out
