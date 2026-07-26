"""Generated from Smithy shape ``com.amazonaws.rds#DBSnapshotAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_snapshot_attribute

DBSnapshotAttributeList: TypeAlias = list[
    "capo_rds.types.db_snapshot_attribute.DBSnapshotAttribute"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSnapshotAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_snapshot_attribute

    for n, item in enumerate(value, 1):
        capo_rds.types.db_snapshot_attribute.serialize_query(
            item, pairs, f"{prefix}.DBSnapshotAttribute.{n}"
        )


def deserialize_query(el: Element) -> DBSnapshotAttributeList:
    import capo_rds.types.db_snapshot_attribute

    out: DBSnapshotAttributeList = []
    for child in el.findall("DBSnapshotAttribute"):
        out.append(capo_rds.types.db_snapshot_attribute.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBSnapshotAttributeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_snapshot_attribute

    for n, item in enumerate(value, 1):
        capo_rds.types.db_snapshot_attribute.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBSnapshotAttributeList:
    import capo_rds.types.db_snapshot_attribute

    out: DBSnapshotAttributeList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_snapshot_attribute.deserialize_query(child))
    return out
