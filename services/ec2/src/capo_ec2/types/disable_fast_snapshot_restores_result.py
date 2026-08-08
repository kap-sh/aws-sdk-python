"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestoresResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.disable_fast_snapshot_restore_error_set
    import capo_ec2.types.disable_fast_snapshot_restore_success_set


class DisableFastSnapshotRestoresResult(TypedDict, closed=True):
    successful: NotRequired[
        "capo_ec2.types.disable_fast_snapshot_restore_success_set.DisableFastSnapshotRestoreSuccessSet"
    ]
    """<p>Information about the snapshots for which fast snapshot restores were successfully disabled.</p>"""
    unsuccessful: NotRequired[
        "capo_ec2.types.disable_fast_snapshot_restore_error_set.DisableFastSnapshotRestoreErrorSet"
    ]
    """<p>Information about the snapshots for which fast snapshot restores could not be disabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableFastSnapshotRestoresResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "successful" in value:
        import capo_ec2.types.disable_fast_snapshot_restore_success_set

        capo_ec2.types.disable_fast_snapshot_restore_success_set.serialize_ec2_query(
            value["successful"], pairs, f"{key_prefix}Successful"
        )
    if "unsuccessful" in value:
        import capo_ec2.types.disable_fast_snapshot_restore_error_set

        capo_ec2.types.disable_fast_snapshot_restore_error_set.serialize_ec2_query(
            value["unsuccessful"], pairs, f"{key_prefix}Unsuccessful"
        )


def deserialize_ec2_query(el: Element) -> DisableFastSnapshotRestoresResult:
    out: DisableFastSnapshotRestoresResult = {}  # type: ignore[typeddict-item]
    if el.find("successful") is not None:
        import capo_ec2.types.disable_fast_snapshot_restore_success_set

        out["successful"] = (
            capo_ec2.types.disable_fast_snapshot_restore_success_set.deserialize_ec2_query(
                el, "successful"
            )
        )
    if el.find("unsuccessful") is not None:
        import capo_ec2.types.disable_fast_snapshot_restore_error_set

        out["unsuccessful"] = (
            capo_ec2.types.disable_fast_snapshot_restore_error_set.deserialize_ec2_query(
                el, "unsuccessful"
            )
        )
    return out
