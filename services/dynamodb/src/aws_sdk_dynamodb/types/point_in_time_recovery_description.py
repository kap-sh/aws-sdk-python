"""Generated from Smithy shape ``com.amazonaws.dynamodb#PointInTimeRecoveryDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.date
    import aws_sdk_dynamodb.types.point_in_time_recovery_status
    import aws_sdk_dynamodb.types.recovery_period_in_days


class PointInTimeRecoveryDescription(TypedDict):
    point_in_time_recovery_status: NotRequired[
        "aws_sdk_dynamodb.types.point_in_time_recovery_status.PointInTimeRecoveryStatus"
    ]
    """<p>The current state of point in time recovery:</p> <ul> <li> <p> <code>ENABLED</code> - Point in time recovery is enabled.</p> </li> <li> <p> <code>DISABLED</code> - Point in time recovery is disabled.</p> </li> </ul>"""
    recovery_period_in_days: NotRequired[
        "aws_sdk_dynamodb.types.recovery_period_in_days.RecoveryPeriodInDays"
    ]
    """<p>The number of preceding days for which continuous backups are taken and maintained. Your table data is only recoverable to any point-in-time from within the configured recovery period. This parameter is optional.</p>"""
    earliest_restorable_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p>Specifies the earliest point in time you can restore your table to. You can restore your table to any point in time during the last 35 days. </p>"""
    latest_restorable_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p> <code>LatestRestorableDateTime</code> is typically 5 minutes before the current time. </p>"""
