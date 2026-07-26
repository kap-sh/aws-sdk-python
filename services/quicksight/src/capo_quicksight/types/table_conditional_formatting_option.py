"""Generated from Smithy shape ``com.amazonaws.quicksight#TableConditionalFormattingOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.table_cell_conditional_formatting
    import capo_quicksight.types.table_row_conditional_formatting


class TableConditionalFormattingOption(TypedDict, closed=True):
    cell: NotRequired[
        "capo_quicksight.types.table_cell_conditional_formatting.TableCellConditionalFormatting"
    ]
    """<p>The cell conditional formatting option for a table.</p>"""
    row: NotRequired[
        "capo_quicksight.types.table_row_conditional_formatting.TableRowConditionalFormatting"
    ]
    """<p>The row conditional formatting option for a table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableConditionalFormattingOption) -> dict:
    out: dict = {}
    if "cell" in value:
        import capo_quicksight.types.table_cell_conditional_formatting

        out["Cell"] = (
            capo_quicksight.types.table_cell_conditional_formatting.serialize_json(
                value["cell"]
            )
        )
    if "row" in value:
        import capo_quicksight.types.table_row_conditional_formatting

        out["Row"] = (
            capo_quicksight.types.table_row_conditional_formatting.serialize_json(
                value["row"]
            )
        )
    return out


def deserialize_json(data: dict) -> TableConditionalFormattingOption:
    out: TableConditionalFormattingOption = {}  # type: ignore[typeddict-item]
    if "Cell" in data:
        import capo_quicksight.types.table_cell_conditional_formatting

        out["cell"] = (
            capo_quicksight.types.table_cell_conditional_formatting.deserialize_json(
                data["Cell"]
            )
        )
    if "Row" in data:
        import capo_quicksight.types.table_row_conditional_formatting

        out["row"] = (
            capo_quicksight.types.table_row_conditional_formatting.deserialize_json(
                data["Row"]
            )
        )
    return out
