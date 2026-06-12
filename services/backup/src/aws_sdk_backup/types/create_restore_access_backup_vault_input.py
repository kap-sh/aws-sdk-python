"""Generated from Smithy shape ``com.amazonaws.backup#CreateRestoreAccessBackupVaultInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_backup.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.requester_comment
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.tags

class CreateRestoreAccessBackupVaultInput(TypedDict):
    source_backup_vault_arn: "aws_sdk_backup.types.arn.ARN"
    """<p>The ARN of the source backup vault containing the recovery points to which temporary access is requested.</p>"""
    backup_vault_name: NotRequired["aws_sdk_backup.types.backup_vault_name.BackupVaultName"]
    """<p>The name of the backup vault to associate with an MPA approval team.</p>"""
    backup_vault_tags: NotRequired["aws_sdk_backup.types.tags.Tags"]
    """<p>Optional tags to assign to the restore access backup vault.</p>"""
    creator_request_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.</p>"""
    requester_comment: NotRequired["aws_sdk_backup.types.requester_comment.RequesterComment"]
    """<p>A comment explaining the reason for requesting restore access to the backup vault.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateRestoreAccessBackupVaultInput) -> dict:
    out: dict = {}
    out["SourceBackupVaultArn"] = value["source_backup_vault_arn"]
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "backup_vault_tags" in value:
        import aws_sdk_backup.types.tags
        out["BackupVaultTags"] = aws_sdk_backup.types.tags.serialize_json(value["backup_vault_tags"])
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "requester_comment" in value:
        out["RequesterComment"] = value["requester_comment"]
    return out


def deserialize_json(data: dict) -> CreateRestoreAccessBackupVaultInput:
    out: CreateRestoreAccessBackupVaultInput = {}  # type: ignore[typeddict-item]
    if "SourceBackupVaultArn" in data:
        out["source_backup_vault_arn"] = data["SourceBackupVaultArn"]
    else:
        raise DeserializationError("CreateRestoreAccessBackupVaultInput.source_backup_vault_arn required")
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    if "BackupVaultTags" in data:
        import aws_sdk_backup.types.tags
        out["backup_vault_tags"] = aws_sdk_backup.types.tags.deserialize_json(data["BackupVaultTags"])
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "RequesterComment" in data:
        out["requester_comment"] = data["RequesterComment"]
    return out