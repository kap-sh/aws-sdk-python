"""Generated from Smithy shape ``com.amazonaws.dynamodb#CreateBackupOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_details


class CreateBackupOutput(TypedDict):
    backup_details: NotRequired["aws_sdk_dynamodb.types.backup_details.BackupDetails"]
    """<p>Contains the details of the backup created for the table.</p>"""
