"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobResultFileGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.snapshot_file_list
    import aws_sdk_quicksight.types.snapshot_job_s3_result_list


class SnapshotJobResultFileGroup(TypedDict):
    files: NotRequired["aws_sdk_quicksight.types.snapshot_file_list.SnapshotFileList"]
    """<p> A list of <code>SnapshotFile</code> objects.</p>"""
    s3_results: NotRequired[
        "aws_sdk_quicksight.types.snapshot_job_s3_result_list.SnapshotJobS3ResultList"
    ]
    """<p> A list of <code>SnapshotJobS3Result</code> objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotJobResultFileGroup) -> dict:
    out: dict = {}
    if "files" in value:
        import aws_sdk_quicksight.types.snapshot_file_list

        out["Files"] = aws_sdk_quicksight.types.snapshot_file_list.serialize_json(
            value["files"]
        )
    if "s3_results" in value:
        import aws_sdk_quicksight.types.snapshot_job_s3_result_list

        out["S3Results"] = (
            aws_sdk_quicksight.types.snapshot_job_s3_result_list.serialize_json(
                value["s3_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotJobResultFileGroup:
    out: SnapshotJobResultFileGroup = {}  # type: ignore[typeddict-item]
    if "Files" in data:
        import aws_sdk_quicksight.types.snapshot_file_list

        out["files"] = aws_sdk_quicksight.types.snapshot_file_list.deserialize_json(
            data["Files"]
        )
    if "S3Results" in data:
        import aws_sdk_quicksight.types.snapshot_job_s3_result_list

        out["s3_results"] = (
            aws_sdk_quicksight.types.snapshot_job_s3_result_list.deserialize_json(
                data["S3Results"]
            )
        )
    return out
