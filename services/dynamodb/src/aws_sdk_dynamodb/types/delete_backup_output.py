"""Generated from Smithy shape ``com.amazonaws.dynamodb#DeleteBackupOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.backup_description


class DeleteBackupOutput(TypedDict):
    backup_description: NotRequired[
        "aws_sdk_dynamodb.types.backup_description.BackupDescription"
    ]
    """<p>Contains the description of the backup created for the table.</p>"""
