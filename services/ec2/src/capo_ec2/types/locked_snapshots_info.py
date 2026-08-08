"""Generated from Smithy shape ``com.amazonaws.ec2#LockedSnapshotsInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cool_off_period_response_hours
    import capo_ec2.types.lock_state
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.retention_period_response_days
    import capo_ec2.types.string


class LockedSnapshotsInfo(TypedDict, closed=True):
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The account ID of the Amazon Web Services account that owns the snapshot.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    lock_state: NotRequired["capo_ec2.types.lock_state.LockState"]
    """<p>The state of the snapshot lock. Valid states include:</p> <ul> <li> <p> <code>compliance-cooloff</code> - The snapshot has been locked in compliance mode but it is still within the cooling-off period. The snapshot can't be deleted, but it can be unlocked and the lock settings can be modified by users with appropriate permissions.</p> </li> <li> <p> <code>governance</code> - The snapshot is locked in governance mode. The snapshot can't be deleted, but it can be unlocked and the lock settings can be modified by users with appropriate permissions.</p> </li> <li> <p> <code>compliance</code> - The snapshot is locked in compliance mode and the cooling-off period has expired. The snapshot can't be unlocked or deleted. The lock duration can only be increased by users with appropriate permissions.</p> </li> <li> <p> <code>expired</code> - The snapshot was locked in compliance or governance mode but the lock duration has expired. The snapshot is not locked and can be deleted.</p> </li> </ul>"""
    lock_duration: NotRequired[
        "capo_ec2.types.retention_period_response_days.RetentionPeriodResponseDays"
    ]
    """<p>The period of time for which the snapshot is locked, in days.</p>"""
    cool_off_period: NotRequired[
        "capo_ec2.types.cool_off_period_response_hours.CoolOffPeriodResponseHours"
    ]
    """<p>The compliance mode cooling-off period, in hours.</p>"""
    cool_off_period_expires_on: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the compliance mode cooling-off period expires, in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""
    lock_created_on: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the snapshot was locked, in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""
    lock_duration_start_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the lock duration started, in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p> <p>If you lock a snapshot that is in the <code>pending</code> state, the lock duration starts only once the snapshot enters the <code>completed</code> state.</p>"""
    lock_expires_on: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the lock will expire, in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LockedSnapshotsInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "lock_state" in value:
        import capo_ec2.types.lock_state

        capo_ec2.types.lock_state.serialize_ec2_query(
            value["lock_state"], pairs, f"{key_prefix}LockState"
        )
    if "lock_duration" in value:
        pairs.append((f"{key_prefix}LockDuration", str(value["lock_duration"])))
    if "cool_off_period" in value:
        pairs.append((f"{key_prefix}CoolOffPeriod", str(value["cool_off_period"])))
    if "cool_off_period_expires_on" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["cool_off_period_expires_on"],
            pairs,
            f"{key_prefix}CoolOffPeriodExpiresOn",
        )
    if "lock_created_on" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["lock_created_on"], pairs, f"{key_prefix}LockCreatedOn"
        )
    if "lock_duration_start_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["lock_duration_start_time"],
            pairs,
            f"{key_prefix}LockDurationStartTime",
        )
    if "lock_expires_on" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["lock_expires_on"], pairs, f"{key_prefix}LockExpiresOn"
        )


def deserialize_ec2_query(el: Element) -> LockedSnapshotsInfo:
    out: LockedSnapshotsInfo = {}  # type: ignore[typeddict-item]
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_snapshot_id = el.find("snapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_lock_state = el.find("lockState")
    if child_lock_state is not None:
        import capo_ec2.types.lock_state

        out["lock_state"] = capo_ec2.types.lock_state.deserialize_ec2_query(
            child_lock_state
        )
    child_lock_duration = el.find("lockDuration")
    if child_lock_duration is not None:
        out["lock_duration"] = int(child_lock_duration.text or "")
    child_cool_off_period = el.find("coolOffPeriod")
    if child_cool_off_period is not None:
        out["cool_off_period"] = int(child_cool_off_period.text or "")
    child_cool_off_period_expires_on = el.find("coolOffPeriodExpiresOn")
    if child_cool_off_period_expires_on is not None:
        import capo_ec2.types.millisecond_date_time

        out["cool_off_period_expires_on"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_cool_off_period_expires_on
            )
        )
    child_lock_created_on = el.find("lockCreatedOn")
    if child_lock_created_on is not None:
        import capo_ec2.types.millisecond_date_time

        out["lock_created_on"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_lock_created_on
            )
        )
    child_lock_duration_start_time = el.find("lockDurationStartTime")
    if child_lock_duration_start_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["lock_duration_start_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_lock_duration_start_time
            )
        )
    child_lock_expires_on = el.find("lockExpiresOn")
    if child_lock_expires_on is not None:
        import capo_ec2.types.millisecond_date_time

        out["lock_expires_on"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_lock_expires_on
            )
        )
    return out
