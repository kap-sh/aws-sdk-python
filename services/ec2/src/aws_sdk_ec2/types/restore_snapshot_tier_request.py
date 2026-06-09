"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreSnapshotTierRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.restore_snapshot_tier_request_temporary_restore_days
    import aws_sdk_ec2.types.snapshot_id


class RestoreSnapshotTierRequest(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot to restore.</p>"""
    temporary_restore_days: NotRequired[
        "aws_sdk_ec2.types.restore_snapshot_tier_request_temporary_restore_days.RestoreSnapshotTierRequestTemporaryRestoreDays"
    ]
    """<p>Specifies the number of days for which to temporarily restore an archived snapshot. Required for temporary restores only. The snapshot will be automatically re-archived after this period.</p> <p>To temporarily restore an archived snapshot, specify the number of days and omit the <b>PermanentRestore</b> parameter or set it to <code>false</code>.</p>"""
    permanent_restore: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to permanently restore an archived snapshot. To permanently restore an archived snapshot, specify <code>true</code> and omit the <b>RestoreSnapshotTierRequest$TemporaryRestoreDays</b> parameter.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RestoreSnapshotTierRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "temporary_restore_days" in value:
        pairs.append(
            (f"{prefix}.TemporaryRestoreDays", str(value["temporary_restore_days"]))
        )
    if "permanent_restore" in value:
        pairs.append(
            (
                f"{prefix}.PermanentRestore",
                "true" if value["permanent_restore"] else "false",
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> RestoreSnapshotTierRequest:
    out: RestoreSnapshotTierRequest = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_temporary_restore_days = el.find("TemporaryRestoreDays")
    if child_temporary_restore_days is not None:
        out["temporary_restore_days"] = int(child_temporary_restore_days.text or "")
    child_permanent_restore = el.find("PermanentRestore")
    if child_permanent_restore is not None:
        out["permanent_restore"] = (
            child_permanent_restore.text or ""
        ).lower() == "true"
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
