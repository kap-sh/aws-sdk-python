"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestoreStateErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.enable_fast_snapshot_restore_state_error_item

EnableFastSnapshotRestoreStateErrorSet: TypeAlias = list[
    "capo_ec2.types.enable_fast_snapshot_restore_state_error_item.EnableFastSnapshotRestoreStateErrorItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableFastSnapshotRestoreStateErrorSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.enable_fast_snapshot_restore_state_error_item

        capo_ec2.types.enable_fast_snapshot_restore_state_error_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> EnableFastSnapshotRestoreStateErrorSet:
    import capo_ec2.types.enable_fast_snapshot_restore_state_error_item

    out: EnableFastSnapshotRestoreStateErrorSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.enable_fast_snapshot_restore_state_error_item.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> EnableFastSnapshotRestoreStateErrorSet:
    import capo_ec2.types.enable_fast_snapshot_restore_state_error_item

    out: EnableFastSnapshotRestoreStateErrorSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.enable_fast_snapshot_restore_state_error_item.deserialize_ec2_query(
                child
            )
        )
    return out
