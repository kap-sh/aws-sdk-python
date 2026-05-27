"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListBackupsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_arn
    import aws_sdk_dynamodb.types.backup_type_filter
    import aws_sdk_dynamodb.types.backups_input_limit
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.time_range_lower_bound
    import aws_sdk_dynamodb.types.time_range_upper_bound


class ListBackupsInput(TypedDict):
    table_name: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p>Lists the backups from the table specified in <code>TableName</code>. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    limit: NotRequired["aws_sdk_dynamodb.types.backups_input_limit.BackupsInputLimit"]
    """<p>Maximum number of backups to return at once.</p>"""
    time_range_lower_bound: NotRequired[
        "aws_sdk_dynamodb.types.time_range_lower_bound.TimeRangeLowerBound"
    ]
    """<p>Only backups created after this time are listed. <code>TimeRangeLowerBound</code> is inclusive.</p>"""
    time_range_upper_bound: NotRequired[
        "aws_sdk_dynamodb.types.time_range_upper_bound.TimeRangeUpperBound"
    ]
    """<p>Only backups created before this time are listed. <code>TimeRangeUpperBound</code> is exclusive. </p>"""
    exclusive_start_backup_arn: NotRequired[
        "aws_sdk_dynamodb.types.backup_arn.BackupArn"
    ]
    """<p> <code>LastEvaluatedBackupArn</code> is the Amazon Resource Name (ARN) of the backup last evaluated when the current page of results was returned, inclusive of the current page of results. This value may be specified as the <code>ExclusiveStartBackupArn</code> of a new <code>ListBackups</code> operation in order to fetch the next page of results. </p>"""
    backup_type: NotRequired[
        "aws_sdk_dynamodb.types.backup_type_filter.BackupTypeFilter"
    ]
    """<p>The backups from the table specified by <code>BackupType</code> are listed.</p> <p>Where <code>BackupType</code> can be:</p> <ul> <li> <p> <code>USER</code> - On-demand backup created by you. (The default setting if no other backup types are specified.)</p> </li> <li> <p> <code>SYSTEM</code> - On-demand backup automatically created by DynamoDB.</p> </li> <li> <p> <code>ALL</code> - All types of on-demand backups (USER and SYSTEM).</p> </li> </ul>"""
