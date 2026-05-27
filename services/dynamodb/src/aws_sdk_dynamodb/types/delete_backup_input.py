"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteBackupInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_arn


class DeleteBackupInput(TypedDict):
    backup_arn: "aws_sdk_dynamodb.types.backup_arn.BackupArn"
    """<p>The ARN associated with the backup.</p>"""
