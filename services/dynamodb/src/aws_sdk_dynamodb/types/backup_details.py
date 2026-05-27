"""Generated from Smithy shape ``com.amazonaws.dynamodb#BackupDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_arn
    import aws_sdk_dynamodb.types.backup_creation_date_time
    import aws_sdk_dynamodb.types.backup_name
    import aws_sdk_dynamodb.types.backup_size_bytes
    import aws_sdk_dynamodb.types.backup_status
    import aws_sdk_dynamodb.types.backup_type
    import aws_sdk_dynamodb.types.date


class BackupDetails(TypedDict):
    backup_arn: "aws_sdk_dynamodb.types.backup_arn.BackupArn"
    """<p>ARN associated with the backup.</p>"""
    backup_name: "aws_sdk_dynamodb.types.backup_name.BackupName"
    """<p>Name of the requested backup.</p>"""
    backup_size_bytes: NotRequired[
        "aws_sdk_dynamodb.types.backup_size_bytes.BackupSizeBytes"
    ]
    """<p>Size of the backup in bytes. DynamoDB updates this value approximately every six hours. Recent changes might not be reflected in this value.</p>"""
    backup_status: "aws_sdk_dynamodb.types.backup_status.BackupStatus"
    """<p>Backup can be in one of the following states: CREATING, ACTIVE, DELETED. </p>"""
    backup_type: "aws_sdk_dynamodb.types.backup_type.BackupType"
    """<p>BackupType:</p> <ul> <li> <p> <code>USER</code> - You create and manage these using the on-demand backup feature.</p> </li> <li> <p> <code>SYSTEM</code> - If you delete a table with point-in-time recovery enabled, a <code>SYSTEM</code> backup is automatically created and is retained for 35 days (at no additional cost). System backups allow you to restore the deleted table to the state it was in just before the point of deletion. </p> </li> <li> <p> <code>AWS_BACKUP</code> - On-demand backup created by you from Backup service.</p> </li> </ul>"""
    backup_creation_date_time: (
        "aws_sdk_dynamodb.types.backup_creation_date_time.BackupCreationDateTime"
    )
    """<p>Time at which the backup was created. This is the request time of the backup. </p>"""
    backup_expiry_date_time: NotRequired["aws_sdk_dynamodb.types.date.Date"]
    """<p>Time at which the automatic on-demand backup created by DynamoDB will expire. This <code>SYSTEM</code> on-demand backup expires automatically 35 days after its creation.</p>"""
