"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSnapshotResultSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.delete_snapshot_return_code

DeleteSnapshotResultSet: TypeAlias = list[
    "capo_ec2.types.delete_snapshot_return_code.DeleteSnapshotReturnCode"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteSnapshotResultSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.delete_snapshot_return_code

        capo_ec2.types.delete_snapshot_return_code.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> DeleteSnapshotResultSet:
    import capo_ec2.types.delete_snapshot_return_code

    out: DeleteSnapshotResultSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.delete_snapshot_return_code.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> DeleteSnapshotResultSet:
    import capo_ec2.types.delete_snapshot_return_code

    out: DeleteSnapshotResultSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.delete_snapshot_return_code.deserialize_ec2_query(child)
        )
    return out
