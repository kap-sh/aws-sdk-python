"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTableTotalOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_total_options
    import capo_quicksight.types.subtotal_options


class PivotTableTotalOptions(TypedDict, closed=True):
    row_subtotal_options: NotRequired[
        "capo_quicksight.types.subtotal_options.SubtotalOptions"
    ]
    """<p>The row subtotal options.</p>"""
    column_subtotal_options: NotRequired[
        "capo_quicksight.types.subtotal_options.SubtotalOptions"
    ]
    """<p>The column subtotal options.</p>"""
    row_total_options: NotRequired[
        "capo_quicksight.types.pivot_total_options.PivotTotalOptions"
    ]
    """<p>The row total options.</p>"""
    column_total_options: NotRequired[
        "capo_quicksight.types.pivot_total_options.PivotTotalOptions"
    ]
    """<p>The column total options.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTableTotalOptions) -> dict:
    out: dict = {}
    if "row_subtotal_options" in value:
        import capo_quicksight.types.subtotal_options

        out["RowSubtotalOptions"] = (
            capo_quicksight.types.subtotal_options.serialize_json(
                value["row_subtotal_options"]
            )
        )
    if "column_subtotal_options" in value:
        import capo_quicksight.types.subtotal_options

        out["ColumnSubtotalOptions"] = (
            capo_quicksight.types.subtotal_options.serialize_json(
                value["column_subtotal_options"]
            )
        )
    if "row_total_options" in value:
        import capo_quicksight.types.pivot_total_options

        out["RowTotalOptions"] = (
            capo_quicksight.types.pivot_total_options.serialize_json(
                value["row_total_options"]
            )
        )
    if "column_total_options" in value:
        import capo_quicksight.types.pivot_total_options

        out["ColumnTotalOptions"] = (
            capo_quicksight.types.pivot_total_options.serialize_json(
                value["column_total_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTableTotalOptions:
    out: PivotTableTotalOptions = {}  # type: ignore[typeddict-item]
    if "RowSubtotalOptions" in data:
        import capo_quicksight.types.subtotal_options

        out["row_subtotal_options"] = (
            capo_quicksight.types.subtotal_options.deserialize_json(
                data["RowSubtotalOptions"]
            )
        )
    if "ColumnSubtotalOptions" in data:
        import capo_quicksight.types.subtotal_options

        out["column_subtotal_options"] = (
            capo_quicksight.types.subtotal_options.deserialize_json(
                data["ColumnSubtotalOptions"]
            )
        )
    if "RowTotalOptions" in data:
        import capo_quicksight.types.pivot_total_options

        out["row_total_options"] = (
            capo_quicksight.types.pivot_total_options.deserialize_json(
                data["RowTotalOptions"]
            )
        )
    if "ColumnTotalOptions" in data:
        import capo_quicksight.types.pivot_total_options

        out["column_total_options"] = (
            capo_quicksight.types.pivot_total_options.deserialize_json(
                data["ColumnTotalOptions"]
            )
        )
    return out
