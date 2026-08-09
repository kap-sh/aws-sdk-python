"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestoreErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.enable_fast_snapshot_restore_error_item

EnableFastSnapshotRestoreErrorSet: TypeAlias = list[
    "capo_ec2.types.enable_fast_snapshot_restore_error_item.EnableFastSnapshotRestoreErrorItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableFastSnapshotRestoreErrorSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.enable_fast_snapshot_restore_error_item

        capo_ec2.types.enable_fast_snapshot_restore_error_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> EnableFastSnapshotRestoreErrorSet:
    import capo_ec2.types.enable_fast_snapshot_restore_error_item

    out: EnableFastSnapshotRestoreErrorSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.enable_fast_snapshot_restore_error_item.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> EnableFastSnapshotRestoreErrorSet:
    import capo_ec2.types.enable_fast_snapshot_restore_error_item

    out: EnableFastSnapshotRestoreErrorSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.enable_fast_snapshot_restore_error_item.deserialize_ec2_query(
                child
            )
        )
    return out
