"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFastSnapshotRestoreSuccessItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.fast_snapshot_restore_state_code
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.string


class DescribeFastSnapshotRestoreSuccessItem(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the snapshot.</p>"""
    availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Availability Zone.</p>"""
    availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Availability Zone.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.fast_snapshot_restore_state_code.FastSnapshotRestoreStateCode"
    ]
    """<p>The state of fast snapshot restores.</p>"""
    state_transition_reason: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The reason for the state transition. The possible values are as follows:</p> <ul> <li> <p> <code>Client.UserInitiated</code> - The state successfully transitioned to <code>enabling</code> or <code>disabling</code>.</p> </li> <li> <p> <code>Client.UserInitiated - Lifecycle state transition</code> - The state successfully transitioned to <code>optimizing</code>, <code>enabled</code>, or <code>disabled</code>.</p> </li> </ul>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that enabled fast snapshot restores on the snapshot.</p>"""
    owner_alias: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services owner alias that enabled fast snapshot restores on the snapshot. This is intended for future use.</p>"""
    enabling_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>enabling</code> state.</p>"""
    optimizing_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>optimizing</code> state.</p>"""
    enabled_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>enabled</code> state.</p>"""
    disabling_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>disabling</code> state.</p>"""
    disabled_time: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time at which fast snapshot restores entered the <code>disabled</code> state.</p>"""
