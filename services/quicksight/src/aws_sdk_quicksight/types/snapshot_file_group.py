"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFileGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.snapshot_file_list


class SnapshotFileGroup(TypedDict, closed=True):
    files: NotRequired["aws_sdk_quicksight.types.snapshot_file_list.SnapshotFileList"]
    """<p>A list of <code>SnapshotFile</code> objects that contain the information on the snapshot files that need to be generated. This structure can hold 1 configuration at a time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotFileGroup) -> dict:
    out: dict = {}
    if "files" in value:
        import aws_sdk_quicksight.types.snapshot_file_list

        out["Files"] = aws_sdk_quicksight.types.snapshot_file_list.serialize_json(
            value["files"]
        )
    return out


def deserialize_json(data: dict) -> SnapshotFileGroup:
    out: SnapshotFileGroup = {}  # type: ignore[typeddict-item]
    if "Files" in data:
        import aws_sdk_quicksight.types.snapshot_file_list

        out["files"] = aws_sdk_quicksight.types.snapshot_file_list.deserialize_json(
            data["Files"]
        )
    return out
