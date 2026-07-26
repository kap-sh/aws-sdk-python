"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobResultFileGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.snapshot_job_result_file_group

SnapshotJobResultFileGroupList: TypeAlias = list[
    "capo_quicksight.types.snapshot_job_result_file_group.SnapshotJobResultFileGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotJobResultFileGroupList) -> list:
    import capo_quicksight.types.snapshot_job_result_file_group

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.snapshot_job_result_file_group.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SnapshotJobResultFileGroupList:
    import capo_quicksight.types.snapshot_job_result_file_group

    out: SnapshotJobResultFileGroupList = []
    for item in data:
        out.append(
            capo_quicksight.types.snapshot_job_result_file_group.deserialize_json(item)
        )
    return out
