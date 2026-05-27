"""Generated from Smithy shape ``com.amazonaws.dynamodb#RestoreSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_arn
    import aws_sdk_dynamodb.types.date
    import aws_sdk_dynamodb.types.restore_in_progress
    import aws_sdk_dynamodb.types.table_arn


class RestoreSummary(TypedDict):
    source_backup_arn: NotRequired["aws_sdk_dynamodb.types.backup_arn.BackupArn"]
    """<p>The Amazon Resource Name (ARN) of the backup from which the table was restored.</p>"""
    source_table_arn: NotRequired["aws_sdk_dynamodb.types.table_arn.TableArn"]
    """<p>The ARN of the source table of the backup that is being restored.</p>"""
    restore_date_time: "aws_sdk_dynamodb.types.date.Date"
    """<p>Point in time or source backup time.</p>"""
    restore_in_progress: "aws_sdk_dynamodb.types.restore_in_progress.RestoreInProgress"
    """<p>Indicates if a restore is in progress or not.</p>"""
