"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableConditionalFormattingOption``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.pivot_table_cell_conditional_formatting


class PivotTableConditionalFormattingOption(TypedDict):
    cell: NotRequired[
        "aws_sdk_quicksight.types.pivot_table_cell_conditional_formatting.PivotTableCellConditionalFormatting"
    ]
    """<p>The cell conditional formatting option for a pivot table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableConditionalFormattingOption) -> dict:
    out: dict = {}
    if "cell" in value:
        import aws_sdk_quicksight.types.pivot_table_cell_conditional_formatting

        out["Cell"] = (
            aws_sdk_quicksight.types.pivot_table_cell_conditional_formatting.serialize_json(
                value["cell"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableConditionalFormattingOption:
    out: PivotTableConditionalFormattingOption = {}  # type: ignore[typeddict-item]
    if "Cell" in data:
        import aws_sdk_quicksight.types.pivot_table_cell_conditional_formatting

        out["cell"] = (
            aws_sdk_quicksight.types.pivot_table_cell_conditional_formatting.deserialize_json(
                data["Cell"]
            )
        )
    return out
