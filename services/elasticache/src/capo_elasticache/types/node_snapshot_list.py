"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeSnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.node_snapshot

NodeSnapshotList: TypeAlias = list["capo_elasticache.types.node_snapshot.NodeSnapshot"]


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeSnapshotList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.node_snapshot

    for n, item in enumerate(value, 1):
        capo_elasticache.types.node_snapshot.serialize_query(
            item, pairs, f"{prefix}.NodeSnapshot.{n}"
        )


def deserialize_query(el: Element) -> NodeSnapshotList:
    import capo_elasticache.types.node_snapshot

    out: NodeSnapshotList = []
    for child in el.findall("NodeSnapshot"):
        out.append(capo_elasticache.types.node_snapshot.deserialize_query(child))
    return out


def serialize_query_flat(
    value: NodeSnapshotList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.node_snapshot

    for n, item in enumerate(value, 1):
        capo_elasticache.types.node_snapshot.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> NodeSnapshotList:
    import capo_elasticache.types.node_snapshot

    out: NodeSnapshotList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.node_snapshot.deserialize_query(child))
    return out
