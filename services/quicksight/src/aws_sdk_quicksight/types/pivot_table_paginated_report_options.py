"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotTablePaginatedReportOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.visibility


class PivotTablePaginatedReportOptions(TypedDict):
    vertical_overflow_visibility: NotRequired[
        "aws_sdk_quicksight.types.visibility.Visibility"
    ]
    """<p>The visibility of the printing table overflow across pages.</p>"""
    overflow_column_header_visibility: NotRequired[
        "aws_sdk_quicksight.types.visibility.Visibility"
    ]
    """<p>The visibility of the repeating header rows on each page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotTablePaginatedReportOptions) -> dict:
    out: dict = {}
    if "vertical_overflow_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["VerticalOverflowVisibility"] = (
            aws_sdk_quicksight.types.visibility.serialize_json(
                value["vertical_overflow_visibility"]
            )
        )
    if "overflow_column_header_visibility" in value:
        import aws_sdk_quicksight.types.visibility

        out["OverflowColumnHeaderVisibility"] = (
            aws_sdk_quicksight.types.visibility.serialize_json(
                value["overflow_column_header_visibility"]
            )
        )
    return out


def deserialize_json(data: dict) -> PivotTablePaginatedReportOptions:
    out: PivotTablePaginatedReportOptions = {}  # type: ignore[typeddict-item]
    if "VerticalOverflowVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["vertical_overflow_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["VerticalOverflowVisibility"]
            )
        )
    if "OverflowColumnHeaderVisibility" in data:
        import aws_sdk_quicksight.types.visibility

        out["overflow_column_header_visibility"] = (
            aws_sdk_quicksight.types.visibility.deserialize_json(
                data["OverflowColumnHeaderVisibility"]
            )
        )
    return out
