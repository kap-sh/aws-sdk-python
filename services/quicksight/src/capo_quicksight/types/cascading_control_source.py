"""Generated from Smithy shape ``com.amazonaws.quicksight#CascadingControlSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.string


class CascadingControlSource(TypedDict, closed=True):
    source_sheet_control_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The source sheet control ID of a <code>CascadingControlSource</code>.</p>"""
    column_to_match: NotRequired[
        "capo_quicksight.types.column_identifier.ColumnIdentifier"
    ]
    """<p>The column identifier that determines which column to look up for the source sheet control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CascadingControlSource) -> dict:
    out: dict = {}
    if "source_sheet_control_id" in value:
        out["SourceSheetControlId"] = value["source_sheet_control_id"]
    if "column_to_match" in value:
        import capo_quicksight.types.column_identifier

        out["ColumnToMatch"] = capo_quicksight.types.column_identifier.serialize_json(
            value["column_to_match"]
        )
    return out


def deserialize_json(data: dict) -> CascadingControlSource:
    out: CascadingControlSource = {}  # type: ignore[typeddict-item]
    if "SourceSheetControlId" in data:
        out["source_sheet_control_id"] = data["SourceSheetControlId"]
    if "ColumnToMatch" in data:
        import capo_quicksight.types.column_identifier

        out["column_to_match"] = (
            capo_quicksight.types.column_identifier.deserialize_json(
                data["ColumnToMatch"]
            )
        )
    return out
