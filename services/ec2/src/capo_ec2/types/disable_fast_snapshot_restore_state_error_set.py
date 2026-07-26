"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestoreStateErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.disable_fast_snapshot_restore_state_error_item

DisableFastSnapshotRestoreStateErrorSet: TypeAlias = list[
    "capo_ec2.types.disable_fast_snapshot_restore_state_error_item.DisableFastSnapshotRestoreStateErrorItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableFastSnapshotRestoreStateErrorSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.disable_fast_snapshot_restore_state_error_item

        capo_ec2.types.disable_fast_snapshot_restore_state_error_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> DisableFastSnapshotRestoreStateErrorSet:
    import capo_ec2.types.disable_fast_snapshot_restore_state_error_item

    out: DisableFastSnapshotRestoreStateErrorSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.disable_fast_snapshot_restore_state_error_item.deserialize_ec2_query(
                child
            )
        )
    return out
