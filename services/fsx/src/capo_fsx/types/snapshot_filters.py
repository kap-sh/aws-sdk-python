"""Generated from Smithy shape ``com.amazonaws.fsx#SnapshotFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.snapshot_filter

SnapshotFilters: TypeAlias = list["capo_fsx.types.snapshot_filter.SnapshotFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotFilters) -> list:
    import capo_fsx.types.snapshot_filter

    out: list = []
    for item in value:
        out.append(capo_fsx.types.snapshot_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SnapshotFilters:
    import capo_fsx.types.snapshot_filter

    out: SnapshotFilters = []
    for item in data:
        out.append(capo_fsx.types.snapshot_filter.deserialize_aws_json_1_1(item))
    return out
