"""Generated from Smithy shape ``com.amazonaws.ec2#LockedSnapshotsInfo``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cool_off_period_response_hours
    import aws_sdk_ec2.types.lock_state
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.retention_period_response_days
    import aws_sdk_ec2.types.string


class LockedSnapshotsInfo(TypedDict):
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The account ID of the Amazon Web Services account that owns the snapshot.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
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
    lock_duration_start_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the lock duration started, in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p> <p>If you lock a snapshot that is in the <code>pending</code> state, the lock duration starts only once the snapshot enters the <code>completed</code> state.</p>"""
    lock_expires_on: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time at which the lock will expire, in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p>"""
