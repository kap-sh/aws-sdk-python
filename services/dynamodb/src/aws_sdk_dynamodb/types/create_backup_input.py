"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateBackupInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_name
    import aws_sdk_dynamodb.types.table_arn


class CreateBackupInput(TypedDict):
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    backup_name: "aws_sdk_dynamodb.types.backup_name.BackupName"
    """<p>Specified name for the backup.</p>"""
