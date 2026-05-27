"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeBackupInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_arn


class DescribeBackupInput(TypedDict):
    backup_arn: "aws_sdk_dynamodb.types.backup_arn.BackupArn"
    """<p>The Amazon Resource Name (ARN) associated with the backup.</p>"""
