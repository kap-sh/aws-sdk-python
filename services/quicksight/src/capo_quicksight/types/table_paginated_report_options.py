"""Generated from Smithy shape ``com.amazonaws.quicksight#TablePaginatedReportOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.visibility


class TablePaginatedReportOptions(TypedDict, closed=True):
    vertical_overflow_visibility: NotRequired[
        "capo_quicksight.types.visibility.Visibility"
    ]
    """<p>The visibility of printing table overflow across pages.</p>"""
    overflow_column_header_visibility: NotRequired[
        "capo_quicksight.types.visibility.Visibility"
    ]
    """<p>The visibility of repeating header rows on each page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TablePaginatedReportOptions) -> dict:
    out: dict = {}
    if "vertical_overflow_visibility" in value:
        import capo_quicksight.types.visibility

        out["VerticalOverflowVisibility"] = (
            capo_quicksight.types.visibility.serialize_json(
                value["vertical_overflow_visibility"]
            )
        )
    if "overflow_column_header_visibility" in value:
        import capo_quicksight.types.visibility

        out["OverflowColumnHeaderVisibility"] = (
            capo_quicksight.types.visibility.serialize_json(
                value["overflow_column_header_visibility"]
            )
        )
    return out


def deserialize_json(data: dict) -> TablePaginatedReportOptions:
    out: TablePaginatedReportOptions = {}  # type: ignore[typeddict-item]
    if "VerticalOverflowVisibility" in data:
        import capo_quicksight.types.visibility

        out["vertical_overflow_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["VerticalOverflowVisibility"]
            )
        )
    if "OverflowColumnHeaderVisibility" in data:
        import capo_quicksight.types.visibility

        out["overflow_column_header_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["OverflowColumnHeaderVisibility"]
            )
        )
    return out
