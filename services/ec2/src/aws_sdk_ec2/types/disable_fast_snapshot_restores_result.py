"""Generated from Smithy shape ``com.amazonaws.ec2#DisableFastSnapshotRestoresResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_fast_snapshot_restore_error_set
    import aws_sdk_ec2.types.disable_fast_snapshot_restore_success_set


class DisableFastSnapshotRestoresResult(TypedDict, closed=True):
    successful: NotRequired[
        "aws_sdk_ec2.types.disable_fast_snapshot_restore_success_set.DisableFastSnapshotRestoreSuccessSet"
    ]
    """<p>Information about the snapshots for which fast snapshot restores were successfully disabled.</p>"""
    unsuccessful: NotRequired[
        "aws_sdk_ec2.types.disable_fast_snapshot_restore_error_set.DisableFastSnapshotRestoreErrorSet"
    ]
    """<p>Information about the snapshots for which fast snapshot restores could not be disabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisableFastSnapshotRestoresResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "successful" in value:
        import aws_sdk_ec2.types.disable_fast_snapshot_restore_success_set

        aws_sdk_ec2.types.disable_fast_snapshot_restore_success_set.serialize_ec2_query(
            value["successful"], pairs, f"{prefix}.Successful"
        )
    if "unsuccessful" in value:
        import aws_sdk_ec2.types.disable_fast_snapshot_restore_error_set

        aws_sdk_ec2.types.disable_fast_snapshot_restore_error_set.serialize_ec2_query(
            value["unsuccessful"], pairs, f"{prefix}.Unsuccessful"
        )


def deserialize_ec2_query(el: Element) -> DisableFastSnapshotRestoresResult:
    out: DisableFastSnapshotRestoresResult = {}  # type: ignore[typeddict-item]
    if el.find("Successful") is not None:
        import aws_sdk_ec2.types.disable_fast_snapshot_restore_success_set

        out["successful"] = (
            aws_sdk_ec2.types.disable_fast_snapshot_restore_success_set.deserialize_ec2_query(
                el, "Successful"
            )
        )
    if el.find("Unsuccessful") is not None:
        import aws_sdk_ec2.types.disable_fast_snapshot_restore_error_set

        out["unsuccessful"] = (
            aws_sdk_ec2.types.disable_fast_snapshot_restore_error_set.deserialize_ec2_query(
                el, "Unsuccessful"
            )
        )
    return out
