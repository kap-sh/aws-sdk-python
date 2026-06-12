"""Generated from Smithy shape ``com.amazonaws.docdb#DBClusterSnapshotAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.db_cluster_snapshot_attribute

DBClusterSnapshotAttributeList: TypeAlias = list[
    "aws_sdk_docdb.types.db_cluster_snapshot_attribute.DBClusterSnapshotAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterSnapshotAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_docdb.types.db_cluster_snapshot_attribute

    for n, item in enumerate(value, 1):
        aws_sdk_docdb.types.db_cluster_snapshot_attribute.serialize_query(
            item, pairs, f"{prefix}.DBClusterSnapshotAttribute.{n}"
        )


def deserialize_query(el: Element) -> DBClusterSnapshotAttributeList:
    import aws_sdk_docdb.types.db_cluster_snapshot_attribute

    out: DBClusterSnapshotAttributeList = []
    for child in el.findall("DBClusterSnapshotAttribute"):
        out.append(
            aws_sdk_docdb.types.db_cluster_snapshot_attribute.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: DBClusterSnapshotAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_docdb.types.db_cluster_snapshot_attribute

    for n, item in enumerate(value, 1):
        aws_sdk_docdb.types.db_cluster_snapshot_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterSnapshotAttributeList:
    import aws_sdk_docdb.types.db_cluster_snapshot_attribute

    out: DBClusterSnapshotAttributeList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_docdb.types.db_cluster_snapshot_attribute.deserialize_query(child)
        )
    return out
