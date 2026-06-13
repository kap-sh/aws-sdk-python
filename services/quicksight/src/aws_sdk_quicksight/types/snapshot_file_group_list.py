"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotFileGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.snapshot_file_group

SnapshotFileGroupList: TypeAlias = list[
    "aws_sdk_quicksight.types.snapshot_file_group.SnapshotFileGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotFileGroupList) -> list:
    import aws_sdk_quicksight.types.snapshot_file_group

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.snapshot_file_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> SnapshotFileGroupList:
    import aws_sdk_quicksight.types.snapshot_file_group

    out: SnapshotFileGroupList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.snapshot_file_group.deserialize_json(item))
    return out
