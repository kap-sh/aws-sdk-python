"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContinuousBackupsDescription``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.continuous_backups_status
    import aws_sdk_dynamodb.types.point_in_time_recovery_description


class ContinuousBackupsDescription(TypedDict):
    continuous_backups_status: (
        "aws_sdk_dynamodb.types.continuous_backups_status.ContinuousBackupsStatus"
    )
    """<p> <code>ContinuousBackupsStatus</code> can be one of the following states: ENABLED, DISABLED</p>"""
    point_in_time_recovery_description: NotRequired[
        "aws_sdk_dynamodb.types.point_in_time_recovery_description.PointInTimeRecoveryDescription"
    ]
    """<p>The description of the point in time recovery settings applied to the table.</p>"""
