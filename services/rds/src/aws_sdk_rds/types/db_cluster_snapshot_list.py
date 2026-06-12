"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterSnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_cluster_snapshot

DBClusterSnapshotList: TypeAlias = list[
    "aws_sdk_rds.types.db_cluster_snapshot.DBClusterSnapshot"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterSnapshotList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_cluster_snapshot

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_cluster_snapshot.serialize_query(
            item, pairs, f"{prefix}.DBClusterSnapshot.{n}"
        )


def deserialize_query(el: Element) -> DBClusterSnapshotList:
    import aws_sdk_rds.types.db_cluster_snapshot

    out: DBClusterSnapshotList = []
    for child in el.findall("DBClusterSnapshot"):
        out.append(aws_sdk_rds.types.db_cluster_snapshot.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBClusterSnapshotList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_cluster_snapshot

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_cluster_snapshot.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterSnapshotList:
    import aws_sdk_rds.types.db_cluster_snapshot

    out: DBClusterSnapshotList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.db_cluster_snapshot.deserialize_query(child))
    return out
