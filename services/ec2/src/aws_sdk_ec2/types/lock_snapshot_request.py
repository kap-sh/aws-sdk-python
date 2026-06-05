"""Generated from Smithy shape ``com.amazonaws.ec2#LockSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.cool_off_period_request_hours
    import aws_sdk_ec2.types.lock_mode
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.retention_period_request_days
    import aws_sdk_ec2.types.snapshot_id


class LockSnapshotRequest(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot to lock.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    lock_mode: NotRequired["aws_sdk_ec2.types.lock_mode.LockMode"]
    """<p>The mode in which to lock the snapshot. Specify one of the following:</p> <ul> <li> <p> <code>governance</code> - Locks the snapshot in governance mode. Snapshots locked in governance mode can't be deleted until one of the following conditions are met:</p> <ul> <li> <p>The lock duration expires.</p> </li> <li> <p>The snapshot is unlocked by a user with the appropriate permissions.</p> </li> </ul> <p>Users with the appropriate IAM permissions can unlock the snapshot, increase or decrease the lock duration, and change the lock mode to <code>compliance</code> at any time.</p> <p>If you lock a snapshot in <code>governance</code> mode, omit <b> CoolOffPeriod</b>.</p> </li> <li> <p> <code>compliance</code> - Locks the snapshot in compliance mode. Snapshots locked in compliance mode can't be unlocked by any user. They can be deleted only after the lock duration expires. Users can't decrease the lock duration or change the lock mode to <code>governance</code>. However, users with appropriate IAM permissions can increase the lock duration at any time.</p> <p>If you lock a snapshot in <code>compliance</code> mode, you can optionally specify <b>CoolOffPeriod</b>.</p> </li> </ul>"""
    cool_off_period: NotRequired[
        "aws_sdk_ec2.types.cool_off_period_request_hours.CoolOffPeriodRequestHours"
    ]
    """<p>The cooling-off period during which you can unlock the snapshot or modify the lock settings after locking the snapshot in compliance mode, in hours. After the cooling-off period expires, you can't unlock or delete the snapshot, decrease the lock duration, or change the lock mode. You can increase the lock duration after the cooling-off period expires.</p> <p>The cooling-off period is optional when locking a snapshot in compliance mode. If you are locking the snapshot in governance mode, omit this parameter.</p> <p>To lock the snapshot in compliance mode immediately without a cooling-off period, omit this parameter.</p> <p>If you are extending the lock duration for a snapshot that is locked in compliance mode after the cooling-off period has expired, omit this parameter. If you specify a cooling-period in a such a request, the request fails.</p> <p>Allowed values: Min 1, max 72.</p>"""
    lock_duration: NotRequired[
        "aws_sdk_ec2.types.retention_period_request_days.RetentionPeriodRequestDays"
    ]
    """<p>The period of time for which to lock the snapshot, in days. The snapshot lock will automatically expire after this period lapses.</p> <p>You must specify either this parameter or <b>ExpirationDate</b>, but not both.</p> <p>Allowed values: Min: 1, max 36500</p>"""
    expiration_date: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the snapshot lock is to automatically expire, in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p> <p>You must specify either this parameter or <b>LockDuration</b>, but not both.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LockSnapshotRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "lock_mode" in value:
        import aws_sdk_ec2.types.lock_mode

        aws_sdk_ec2.types.lock_mode.serialize_ec2_query(
            value["lock_mode"], pairs, f"{prefix}.LockMode"
        )
    if "cool_off_period" in value:
        pairs.append((f"{prefix}.CoolOffPeriod", str(value["cool_off_period"])))
    if "lock_duration" in value:
        pairs.append((f"{prefix}.LockDuration", str(value["lock_duration"])))
    if "expiration_date" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["expiration_date"], pairs, f"{prefix}.ExpirationDate"
        )


def deserialize_ec2_query(el: Element) -> LockSnapshotRequest:
    out: LockSnapshotRequest = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_lock_mode = el.find("LockMode")
    if child_lock_mode is not None:
        import aws_sdk_ec2.types.lock_mode

        out["lock_mode"] = aws_sdk_ec2.types.lock_mode.deserialize_ec2_query(
            child_lock_mode
        )
    child_cool_off_period = el.find("CoolOffPeriod")
    if child_cool_off_period is not None:
        out["cool_off_period"] = int(child_cool_off_period.text or "")
    child_lock_duration = el.find("LockDuration")
    if child_lock_duration is not None:
        out["lock_duration"] = int(child_lock_duration.text or "")
    child_expiration_date = el.find("ExpirationDate")
    if child_expiration_date is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["expiration_date"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_expiration_date
            )
        )
    return out
