"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteClusterSnapshotMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.delete_cluster_snapshot_message

DeleteClusterSnapshotMessageList: TypeAlias = list[
    "capo_redshift.types.delete_cluster_snapshot_message.DeleteClusterSnapshotMessage"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteClusterSnapshotMessageList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.delete_cluster_snapshot_message

    for n, item in enumerate(value, 1):
        capo_redshift.types.delete_cluster_snapshot_message.serialize_query(
            item, pairs, f"{prefix}.DeleteClusterSnapshotMessage.{n}"
        )


def deserialize_query(el: Element) -> DeleteClusterSnapshotMessageList:
    import capo_redshift.types.delete_cluster_snapshot_message

    out: DeleteClusterSnapshotMessageList = []
    for child in el.findall("DeleteClusterSnapshotMessage"):
        out.append(
            capo_redshift.types.delete_cluster_snapshot_message.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: DeleteClusterSnapshotMessageList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.delete_cluster_snapshot_message

    for n, item in enumerate(value, 1):
        capo_redshift.types.delete_cluster_snapshot_message.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> DeleteClusterSnapshotMessageList:
    import capo_redshift.types.delete_cluster_snapshot_message

    out: DeleteClusterSnapshotMessageList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.delete_cluster_snapshot_message.deserialize_query(child)
        )
    return out
