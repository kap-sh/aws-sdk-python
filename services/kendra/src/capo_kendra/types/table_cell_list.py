"""Generated from Smithy shape ``com.amazonaws.kendra#TableCellList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.table_cell

TableCellList: TypeAlias = list["capo_kendra.types.table_cell.TableCell"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableCellList) -> list:
    import capo_kendra.types.table_cell

    out: list = []
    for item in value:
        out.append(capo_kendra.types.table_cell.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TableCellList:
    import capo_kendra.types.table_cell

    out: TableCellList = []
    for item in data:
        out.append(capo_kendra.types.table_cell.deserialize_aws_json_1_1(item))
    return out
