"""Generated from Smithy shape ``com.amazonaws.elasticache#SnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.snapshot

SnapshotList: TypeAlias = list["capo_elasticache.types.snapshot.Snapshot"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.snapshot

    for n, item in enumerate(value, 1):
        capo_elasticache.types.snapshot.serialize_query(
            item, pairs, f"{prefix}.Snapshot.{n}"
        )


def deserialize_query(el: Element) -> SnapshotList:
    import capo_elasticache.types.snapshot

    out: SnapshotList = []
    for child in el.findall("Snapshot"):
        out.append(capo_elasticache.types.snapshot.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SnapshotList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.snapshot

    for n, item in enumerate(value, 1):
        capo_elasticache.types.snapshot.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> SnapshotList:
    import capo_elasticache.types.snapshot

    out: SnapshotList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.snapshot.deserialize_query(child))
    return out
