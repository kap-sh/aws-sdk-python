"""Generated from Smithy shape ``com.amazonaws.securityhub#Cell``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.long
    import capo_securityhub.types.non_empty_string


class Cell(TypedDict, closed=True):
    column: NotRequired["capo_securityhub.types.long.Long"]
    """<p>The column number of the column that contains the data. For a Microsoft Excel workbook, the column number corresponds to the alphabetical column identifiers. For example, a value of 1 for Column corresponds to the A column in the workbook.</p>"""
    row: NotRequired["capo_securityhub.types.long.Long"]
    """<p>The row number of the row that contains the data.</p>"""
    column_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the column that contains the data.</p>"""
    cell_reference: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>For a Microsoft Excel workbook, provides the location of the cell, as an absolute cell reference, that contains the data. For example, Sheet2!C5 for cell C5 on Sheet2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cell) -> dict:
    out: dict = {}
    if "column" in value:
        out["Column"] = value["column"]
    if "row" in value:
        out["Row"] = value["row"]
    if "column_name" in value:
        out["ColumnName"] = value["column_name"]
    if "cell_reference" in value:
        out["CellReference"] = value["cell_reference"]
    return out


def deserialize_json(data: dict) -> Cell:
    out: Cell = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        out["column"] = data["Column"]
    if "Row" in data:
        out["row"] = data["Row"]
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    if "CellReference" in data:
        out["cell_reference"] = data["CellReference"]
    return out
