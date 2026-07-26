"""Generated from Smithy shape ``com.amazonaws.docdbelastic#ClusterSnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_docdb_elastic.types.cluster_snapshot_in_list

ClusterSnapshotList: TypeAlias = list[
    "capo_docdb_elastic.types.cluster_snapshot_in_list.ClusterSnapshotInList"
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterSnapshotList) -> list:
    import capo_docdb_elastic.types.cluster_snapshot_in_list

    out: list = []
    for item in value:
        out.append(
            capo_docdb_elastic.types.cluster_snapshot_in_list.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ClusterSnapshotList:
    import capo_docdb_elastic.types.cluster_snapshot_in_list

    out: ClusterSnapshotList = []
    for item in data:
        out.append(
            capo_docdb_elastic.types.cluster_snapshot_in_list.deserialize_json(item)
        )
    return out
