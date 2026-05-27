"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListBackupsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_arn
    import aws_sdk_dynamodb.types.backup_summaries


class ListBackupsOutput(TypedDict):
    backup_summaries: NotRequired[
        "aws_sdk_dynamodb.types.backup_summaries.BackupSummaries"
    ]
    """<p>List of <code>BackupSummary</code> objects.</p>"""
    last_evaluated_backup_arn: NotRequired[
        "aws_sdk_dynamodb.types.backup_arn.BackupArn"
    ]
    """<p> The ARN of the backup last evaluated when the current page of results was returned, inclusive of the current page of results. This value may be specified as the <code>ExclusiveStartBackupArn</code> of a new <code>ListBackups</code> operation in order to fetch the next page of results. </p> <p> If <code>LastEvaluatedBackupArn</code> is empty, then the last page of results has been processed and there are no more results to be retrieved. </p> <p> If <code>LastEvaluatedBackupArn</code> is not empty, this may or may not indicate that there is more data to be returned. All results are guaranteed to have been returned if and only if no value for <code>LastEvaluatedBackupArn</code> is returned. </p>"""
