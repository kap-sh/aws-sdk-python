"""Generated from Smithy shape ``com.amazonaws.elasticache#SnapshotArnsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string

SnapshotArnsList: TypeAlias = list["capo_elasticache.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotArnsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.SnapshotArn.{n}", str(item)))


def deserialize_query(el: Element) -> SnapshotArnsList:
    out: SnapshotArnsList = []
    for child in el.findall("SnapshotArn"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: SnapshotArnsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> SnapshotArnsList:
    out: SnapshotArnsList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
