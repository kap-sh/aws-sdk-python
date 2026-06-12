"""Generated from Smithy shape ``com.amazonaws.fsx#SnapshotFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fsx.types.snapshot_filter_value

SnapshotFilterValues: TypeAlias = list[
    "aws_sdk_fsx.types.snapshot_filter_value.SnapshotFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SnapshotFilterValues:
    return list(data)
