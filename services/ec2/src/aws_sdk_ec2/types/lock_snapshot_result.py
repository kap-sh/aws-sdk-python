"""Generated from Smithy shape ``com.amazonaws.ec2#LockSnapshotResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cool_off_period_response_hours
    import aws_sdk_ec2.types.lock_state
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.retention_period_response_days
    import aws_sdk_ec2.types.string


class LockSnapshotResult(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot</p>"""
    lock_state: NotRequired["aws_sdk_ec2.types.lock_state.LockState"]
    """<p>The state of the snapshot lock. Valid states include:</p> <ul> <li> <p> <code>compliance-cooloff</code> - The snapshot has been locked in compliance mode but it is still within the cooling-off period. The snapshot can't be deleted, but it can be unlocked and the lock settings can be modified by users with appropriate permissions.</p> </li> <li> <p> <code>governance</code> - The snapshot is locked in governance mode. The snapshot can't be deleted, but it can be unlocked and the lock settings can be modified by users with appropriate permissions.</p> </li> <li> <p> <code>compliance</code> - The snapshot is locked in compliance mode and the cooling-off period has expired. The snapshot can't be unlocked or deleted. The lock duration can only be increased by users with appropriate permissions.</p> </li> <li> <p> <code>expired</code> - The snapshot was locked in compliance or governance mode but the lock duration has expired. The snapshot is not locked and can be deleted.</p> </li> </ul>"""
    lock_duration: NotRequired[
        "aws_sdk_ec2.types.retention_period_response_days.RetentionPeriodResponseDays"
    ]
    """<p>The period of time for which the snapshot is locked, in days.</p>"""
    cool_off_period: NotRequired[
        "aws_sdk_ec2.types.cool_off_period_response_hours.CoolOffPeriodResponseHours"
    ]
    """<p>The compliance mode cooling-off period, in hours.</p>"""
    cool_off_period_expires_on: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the compliance mode cooling-off period expires, in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""
    lock_created_on: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the snapshot was locked, in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""
    lock_expires_on: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the lock will expire, in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""
    lock_duration_start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the lock duration started, in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LockSnapshotResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_id" in value:
        pairs.append((f"{prefix}.SnapshotId", str(value["snapshot_id"])))
    if "lock_state" in value:
        import aws_sdk_ec2.types.lock_state

        aws_sdk_ec2.types.lock_state.serialize_ec2_query(
            value["lock_state"], pairs, f"{prefix}.LockState"
        )
    if "lock_duration" in value:
        pairs.append((f"{prefix}.LockDuration", str(value["lock_duration"])))
    if "cool_off_period" in value:
        pairs.append((f"{prefix}.CoolOffPeriod", str(value["cool_off_period"])))
    if "cool_off_period_expires_on" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["cool_off_period_expires_on"],
            pairs,
            f"{prefix}.CoolOffPeriodExpiresOn",
        )
    if "lock_created_on" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["lock_created_on"], pairs, f"{prefix}.LockCreatedOn"
        )
    if "lock_expires_on" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["lock_expires_on"], pairs, f"{prefix}.LockExpiresOn"
        )
    if "lock_duration_start_time" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["lock_duration_start_time"], pairs, f"{prefix}.LockDurationStartTime"
        )


def deserialize_ec2_query(el: Element) -> LockSnapshotResult:
    out: LockSnapshotResult = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_lock_state = el.find("LockState")
    if child_lock_state is not None:
        import aws_sdk_ec2.types.lock_state

        out["lock_state"] = aws_sdk_ec2.types.lock_state.deserialize_ec2_query(
            child_lock_state
        )
    child_lock_duration = el.find("LockDuration")
    if child_lock_duration is not None:
        out["lock_duration"] = int(child_lock_duration.text or "")
    child_cool_off_period = el.find("CoolOffPeriod")
    if child_cool_off_period is not None:
        out["cool_off_period"] = int(child_cool_off_period.text or "")
    child_cool_off_period_expires_on = el.find("CoolOffPeriodExpiresOn")
    if child_cool_off_period_expires_on is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["cool_off_period_expires_on"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_cool_off_period_expires_on
            )
        )
    child_lock_created_on = el.find("LockCreatedOn")
    if child_lock_created_on is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["lock_created_on"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_lock_created_on
            )
        )
    child_lock_expires_on = el.find("LockExpiresOn")
    if child_lock_expires_on is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["lock_expires_on"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_lock_expires_on
            )
        )
    child_lock_duration_start_time = el.find("LockDurationStartTime")
    if child_lock_duration_start_time is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["lock_duration_start_time"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_lock_duration_start_time
            )
        )
    return out
