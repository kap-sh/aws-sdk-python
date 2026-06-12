"""Generated from Smithy shape ``com.amazonaws.kendra#TableRow``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.table_cell_list


class TableRow(TypedDict):
    cells: NotRequired["aws_sdk_kendra.types.table_cell_list.TableCellList"]
    """<p>A list of table cells in a row.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableRow) -> dict:
    out: dict = {}
    if "cells" in value:
        import aws_sdk_kendra.types.table_cell_list

        out["Cells"] = aws_sdk_kendra.types.table_cell_list.serialize_aws_json_1_1(
            value["cells"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TableRow:
    out: TableRow = {}  # type: ignore[typeddict-item]
    if "Cells" in data:
        import aws_sdk_kendra.types.table_cell_list

        out["cells"] = aws_sdk_kendra.types.table_cell_list.deserialize_aws_json_1_1(
            data["Cells"]
        )
    return out
