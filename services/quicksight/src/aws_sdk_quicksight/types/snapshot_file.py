"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFile``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.snapshot_file_format_type
    import aws_sdk_quicksight.types.snapshot_file_sheet_selection_list


class SnapshotFile(TypedDict):
    sheet_selections: "aws_sdk_quicksight.types.snapshot_file_sheet_selection_list.SnapshotFileSheetSelectionList"
    """<p>A list of <code>SnapshotFileSheetSelection</code> objects that contain information on the dashboard sheet that is exported. These objects provide information about the snapshot artifacts that are generated during the job. This structure can hold a maximum of 5 CSV configurations, 5 Excel configurations, or 1 configuration for PDF.</p>"""
    format_type: (
        "aws_sdk_quicksight.types.snapshot_file_format_type.SnapshotFileFormatType"
    )
    """<p>The format of the snapshot file to be generated. You can choose between <code>CSV</code>, <code>Excel</code>, or <code>PDF</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotFile) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.snapshot_file_sheet_selection_list

    out["SheetSelections"] = (
        aws_sdk_quicksight.types.snapshot_file_sheet_selection_list.serialize_json(
            value["sheet_selections"]
        )
    )
    import aws_sdk_quicksight.types.snapshot_file_format_type

    out["FormatType"] = (
        aws_sdk_quicksight.types.snapshot_file_format_type.serialize_json(
            value["format_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> SnapshotFile:
    out: SnapshotFile = {}  # type: ignore[typeddict-item]
    if "SheetSelections" in data:
        import aws_sdk_quicksight.types.snapshot_file_sheet_selection_list

        out["sheet_selections"] = (
            aws_sdk_quicksight.types.snapshot_file_sheet_selection_list.deserialize_json(
                data["SheetSelections"]
            )
        )
    else:
        raise DeserializationError("SnapshotFile.sheet_selections required")
    if "FormatType" in data:
        import aws_sdk_quicksight.types.snapshot_file_format_type

        out["format_type"] = (
            aws_sdk_quicksight.types.snapshot_file_format_type.deserialize_json(
                data["FormatType"]
            )
        )
    else:
        raise DeserializationError("SnapshotFile.format_type required")
    return out
