"""Generated from Smithy shape ``com.amazonaws.ec2#EnableFastSnapshotRestoresResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.enable_fast_snapshot_restore_error_set
    import capo_ec2.types.enable_fast_snapshot_restore_success_set


class EnableFastSnapshotRestoresResult(TypedDict, closed=True):
    successful: NotRequired[
        "capo_ec2.types.enable_fast_snapshot_restore_success_set.EnableFastSnapshotRestoreSuccessSet"
    ]
    """<p>Information about the snapshots for which fast snapshot restores were successfully enabled.</p>"""
    unsuccessful: NotRequired[
        "capo_ec2.types.enable_fast_snapshot_restore_error_set.EnableFastSnapshotRestoreErrorSet"
    ]
    """<p>Information about the snapshots for which fast snapshot restores could not be enabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnableFastSnapshotRestoresResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "successful" in value:
        import capo_ec2.types.enable_fast_snapshot_restore_success_set

        capo_ec2.types.enable_fast_snapshot_restore_success_set.serialize_ec2_query(
            value["successful"], pairs, f"{prefix}.Successful"
        )
    if "unsuccessful" in value:
        import capo_ec2.types.enable_fast_snapshot_restore_error_set

        capo_ec2.types.enable_fast_snapshot_restore_error_set.serialize_ec2_query(
            value["unsuccessful"], pairs, f"{prefix}.Unsuccessful"
        )


def deserialize_ec2_query(el: Element) -> EnableFastSnapshotRestoresResult:
    out: EnableFastSnapshotRestoresResult = {}  # type: ignore[typeddict-item]
    if el.find("Successful") is not None:
        import capo_ec2.types.enable_fast_snapshot_restore_success_set

        out["successful"] = (
            capo_ec2.types.enable_fast_snapshot_restore_success_set.deserialize_ec2_query(
                el, "Successful"
            )
        )
    if el.find("Unsuccessful") is not None:
        import capo_ec2.types.enable_fast_snapshot_restore_error_set

        out["unsuccessful"] = (
            capo_ec2.types.enable_fast_snapshot_restore_error_set.deserialize_ec2_query(
                el, "Unsuccessful"
            )
        )
    return out
