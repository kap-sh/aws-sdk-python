"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ClusterSnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.cluster_snapshot_in_list

ClusterSnapshotList: TypeAlias = list[
    "aws_sdk_docdb_elastic.types.cluster_snapshot_in_list.ClusterSnapshotInList"
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterSnapshotList) -> list:
    import aws_sdk_docdb_elastic.types.cluster_snapshot_in_list

    out: list = []
    for item in value:
        out.append(
            aws_sdk_docdb_elastic.types.cluster_snapshot_in_list.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ClusterSnapshotList:
    import aws_sdk_docdb_elastic.types.cluster_snapshot_in_list

    out: ClusterSnapshotList = []
    for item in data:
        out.append(
            aws_sdk_docdb_elastic.types.cluster_snapshot_in_list.deserialize_json(item)
        )
    return out
