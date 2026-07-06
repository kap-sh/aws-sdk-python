"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisteredUserSnapshotJobResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.snapshot_job_result_file_group_list


class RegisteredUserSnapshotJobResult(TypedDict, closed=True):
    file_groups: NotRequired[
        "aws_sdk_quicksight.types.snapshot_job_result_file_group_list.SnapshotJobResultFileGroupList"
    ]
    """<p>A list of <code>SnapshotJobResultFileGroup</code> objects that contain information on the files that are requested for registered user during a <code>StartDashboardSnapshotJob</code> API call. If the job succeeds, these objects contain the location where the snapshot artifacts are stored. If the job fails, the objects contain information about the error that caused the job to fail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredUserSnapshotJobResult) -> dict:
    out: dict = {}
    if "file_groups" in value:
        import aws_sdk_quicksight.types.snapshot_job_result_file_group_list

        out["FileGroups"] = (
            aws_sdk_quicksight.types.snapshot_job_result_file_group_list.serialize_json(
                value["file_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisteredUserSnapshotJobResult:
    out: RegisteredUserSnapshotJobResult = {}  # type: ignore[typeddict-item]
    if "FileGroups" in data:
        import aws_sdk_quicksight.types.snapshot_job_result_file_group_list

        out["file_groups"] = (
            aws_sdk_quicksight.types.snapshot_job_result_file_group_list.deserialize_json(
                data["FileGroups"]
            )
        )
    return out
