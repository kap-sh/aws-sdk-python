"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobResultErrorInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.snapshot_job_result_error_info

SnapshotJobResultErrorInfoList: TypeAlias = list[
    "aws_sdk_quicksight.types.snapshot_job_result_error_info.SnapshotJobResultErrorInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotJobResultErrorInfoList) -> list:
    import aws_sdk_quicksight.types.snapshot_job_result_error_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.snapshot_job_result_error_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SnapshotJobResultErrorInfoList:
    import aws_sdk_quicksight.types.snapshot_job_result_error_info

    out: SnapshotJobResultErrorInfoList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.snapshot_job_result_error_info.deserialize_json(
                item
            )
        )
    return out
