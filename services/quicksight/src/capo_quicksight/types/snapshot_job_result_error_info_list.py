"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobResultErrorInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.snapshot_job_result_error_info

SnapshotJobResultErrorInfoList: TypeAlias = list[
    "capo_quicksight.types.snapshot_job_result_error_info.SnapshotJobResultErrorInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotJobResultErrorInfoList) -> list:
    import capo_quicksight.types.snapshot_job_result_error_info

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.snapshot_job_result_error_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SnapshotJobResultErrorInfoList:
    import capo_quicksight.types.snapshot_job_result_error_info

    out: SnapshotJobResultErrorInfoList = []
    for item in data:
        out.append(
            capo_quicksight.types.snapshot_job_result_error_info.deserialize_json(item)
        )
    return out
