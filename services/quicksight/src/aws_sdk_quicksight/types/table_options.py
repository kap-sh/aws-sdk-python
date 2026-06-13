"""Generated from Smithy shape ``com.amazonaws.quicksight#TableOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.row_alternate_color_options
    import aws_sdk_quicksight.types.table_cell_style
    import aws_sdk_quicksight.types.table_orientation


class TableOptions(TypedDict):
    orientation: NotRequired[
        "aws_sdk_quicksight.types.table_orientation.TableOrientation"
    ]
    """<p>The orientation (vertical, horizontal) for a table.</p>"""
    header_style: NotRequired[
        "aws_sdk_quicksight.types.table_cell_style.TableCellStyle"
    ]
    """<p>The table cell style of a table header.</p>"""
    cell_style: NotRequired["aws_sdk_quicksight.types.table_cell_style.TableCellStyle"]
    """<p>The table cell style of table cells.</p>"""
    row_alternate_color_options: NotRequired[
        "aws_sdk_quicksight.types.row_alternate_color_options.RowAlternateColorOptions"
    ]
    """<p>The row alternate color options (widget status, row alternate colors) for a table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableOptions) -> dict:
    out: dict = {}
    if "orientation" in value:
        import aws_sdk_quicksight.types.table_orientation

        out["Orientation"] = aws_sdk_quicksight.types.table_orientation.serialize_json(
            value["orientation"]
        )
    if "header_style" in value:
        import aws_sdk_quicksight.types.table_cell_style

        out["HeaderStyle"] = aws_sdk_quicksight.types.table_cell_style.serialize_json(
            value["header_style"]
        )
    if "cell_style" in value:
        import aws_sdk_quicksight.types.table_cell_style

        out["CellStyle"] = aws_sdk_quicksight.types.table_cell_style.serialize_json(
            value["cell_style"]
        )
    if "row_alternate_color_options" in value:
        import aws_sdk_quicksight.types.row_alternate_color_options

        out["RowAlternateColorOptions"] = (
            aws_sdk_quicksight.types.row_alternate_color_options.serialize_json(
                value["row_alternate_color_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableOptions:
    out: TableOptions = {}  # type: ignore[typeddict-item]
    if "Orientation" in data:
        import aws_sdk_quicksight.types.table_orientation

        out["orientation"] = (
            aws_sdk_quicksight.types.table_orientation.deserialize_json(
                data["Orientation"]
            )
        )
    if "HeaderStyle" in data:
        import aws_sdk_quicksight.types.table_cell_style

        out["header_style"] = (
            aws_sdk_quicksight.types.table_cell_style.deserialize_json(
                data["HeaderStyle"]
            )
        )
    if "CellStyle" in data:
        import aws_sdk_quicksight.types.table_cell_style

        out["cell_style"] = aws_sdk_quicksight.types.table_cell_style.deserialize_json(
            data["CellStyle"]
        )
    if "RowAlternateColorOptions" in data:
        import aws_sdk_quicksight.types.row_alternate_color_options

        out["row_alternate_color_options"] = (
            aws_sdk_quicksight.types.row_alternate_color_options.deserialize_json(
                data["RowAlternateColorOptions"]
            )
        )
    return out
