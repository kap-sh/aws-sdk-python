"""Generated from Smithy shape ``com.amazonaws.fsx#SnapshotIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.snapshot_id

SnapshotIds: TypeAlias = list["aws_sdk_fsx.types.snapshot_id.SnapshotId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SnapshotIds:
    return list(data)
