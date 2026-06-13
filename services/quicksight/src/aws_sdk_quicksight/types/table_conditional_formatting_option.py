"""Generated from Smithy shape ``com.amazonaws.quicksight#TableConditionalFormattingOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_cell_conditional_formatting
    import aws_sdk_quicksight.types.table_row_conditional_formatting


class TableConditionalFormattingOption(TypedDict):
    cell: NotRequired[
        "aws_sdk_quicksight.types.table_cell_conditional_formatting.TableCellConditionalFormatting"
    ]
    """<p>The cell conditional formatting option for a table.</p>"""
    row: NotRequired[
        "aws_sdk_quicksight.types.table_row_conditional_formatting.TableRowConditionalFormatting"
    ]
    """<p>The row conditional formatting option for a table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableConditionalFormattingOption) -> dict:
    out: dict = {}
    if "cell" in value:
        import aws_sdk_quicksight.types.table_cell_conditional_formatting

        out["Cell"] = (
            aws_sdk_quicksight.types.table_cell_conditional_formatting.serialize_json(
                value["cell"]
            )
        )
    if "row" in value:
        import aws_sdk_quicksight.types.table_row_conditional_formatting

        out["Row"] = (
            aws_sdk_quicksight.types.table_row_conditional_formatting.serialize_json(
                value["row"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableConditionalFormattingOption:
    out: TableConditionalFormattingOption = {}  # type: ignore[typeddict-item]
    if "Cell" in data:
        import aws_sdk_quicksight.types.table_cell_conditional_formatting

        out["cell"] = (
            aws_sdk_quicksight.types.table_cell_conditional_formatting.deserialize_json(
                data["Cell"]
            )
        )
    if "Row" in data:
        import aws_sdk_quicksight.types.table_row_conditional_formatting

        out["row"] = (
            aws_sdk_quicksight.types.table_row_conditional_formatting.deserialize_json(
                data["Row"]
            )
        )
    return out
