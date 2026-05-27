"""Generated from Smithy shape ``com.amazonaws.dynamodb#PointInTimeRecoverySpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.boolean_object
    import aws_sdk_dynamodb.types.recovery_period_in_days


class PointInTimeRecoverySpecification(TypedDict):
    point_in_time_recovery_enabled: (
        "aws_sdk_dynamodb.types.boolean_object.BooleanObject"
    )
    """<p>Indicates whether point in time recovery is enabled (true) or disabled (false) on the table.</p>"""
    recovery_period_in_days: NotRequired[
        "aws_sdk_dynamodb.types.recovery_period_in_days.RecoveryPeriodInDays"
    ]
    """<p>The number of preceding days for which continuous backups are taken and maintained. Your table data is only recoverable to any point-in-time from within the configured recovery period. This parameter is optional. If no value is provided, the value will default to 35.</p>"""
