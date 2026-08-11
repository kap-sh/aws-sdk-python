"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterSnapshotAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster_snapshot_attribute

DBClusterSnapshotAttributeList: TypeAlias = list[
    "capo_rds.types.db_cluster_snapshot_attribute.DBClusterSnapshotAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterSnapshotAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_snapshot_attribute

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_snapshot_attribute.serialize_query(
            item, pairs, f"{prefix}.DBClusterSnapshotAttribute.{n}"
        )


def deserialize_query(el: Element) -> DBClusterSnapshotAttributeList:
    import capo_rds.types.db_cluster_snapshot_attribute

    out: DBClusterSnapshotAttributeList = []
    for child in el.findall("DBClusterSnapshotAttribute"):
        out.append(
            capo_rds.types.db_cluster_snapshot_attribute.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: DBClusterSnapshotAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster_snapshot_attribute

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster_snapshot_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterSnapshotAttributeList:
    import capo_rds.types.db_cluster_snapshot_attribute

    out: DBClusterSnapshotAttributeList = []
    for child in parent.findall(tag):
        out.append(
            capo_rds.types.db_cluster_snapshot_attribute.deserialize_query(child)
        )
    return out
