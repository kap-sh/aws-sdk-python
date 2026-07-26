"""Generated from Smithy shape ``com.amazonaws.redshift#SnapshotCopyGrantList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.snapshot_copy_grant

SnapshotCopyGrantList: TypeAlias = list[
    "capo_redshift.types.snapshot_copy_grant.SnapshotCopyGrant"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SnapshotCopyGrantList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.snapshot_copy_grant

    for n, item in enumerate(value, 1):
        capo_redshift.types.snapshot_copy_grant.serialize_query(
            item, pairs, f"{prefix}.SnapshotCopyGrant.{n}"
        )


def deserialize_query(el: Element) -> SnapshotCopyGrantList:
    import capo_redshift.types.snapshot_copy_grant

    out: SnapshotCopyGrantList = []
    for child in el.findall("SnapshotCopyGrant"):
        out.append(capo_redshift.types.snapshot_copy_grant.deserialize_query(child))
    return out


def serialize_query_flat(
    value: SnapshotCopyGrantList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.snapshot_copy_grant

    for n, item in enumerate(value, 1):
        capo_redshift.types.snapshot_copy_grant.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SnapshotCopyGrantList:
    import capo_redshift.types.snapshot_copy_grant

    out: SnapshotCopyGrantList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.snapshot_copy_grant.deserialize_query(child))
    return out
