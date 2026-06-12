"""Generated from Smithy shape ``com.amazonaws.rds#DBSnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_snapshot

DBSnapshotList: TypeAlias = list["aws_sdk_rds.types.db_snapshot.DBSnapshot"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSnapshotList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_snapshot

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_snapshot.serialize_query(
            item, pairs, f"{prefix}.DBSnapshot.{n}"
        )


def deserialize_query(el: Element) -> DBSnapshotList:
    import aws_sdk_rds.types.db_snapshot

    out: DBSnapshotList = []
    for child in el.findall("DBSnapshot"):
        out.append(aws_sdk_rds.types.db_snapshot.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBSnapshotList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.db_snapshot

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.db_snapshot.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBSnapshotList:
    import aws_sdk_rds.types.db_snapshot

    out: DBSnapshotList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.db_snapshot.deserialize_query(child))
    return out
