"""Generated from Smithy shape ``com.amazonaws.directoryservice#SnapshotIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.snapshot_id

SnapshotIds: TypeAlias = list["capo_directory_service.types.snapshot_id.SnapshotId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SnapshotIds:
    return list(data)
