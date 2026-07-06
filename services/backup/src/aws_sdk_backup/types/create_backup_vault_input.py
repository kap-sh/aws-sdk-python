"""Generated from Smithy shape ``com.amazonaws.backup#CreateBackupVaultInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.string
    import aws_sdk_backup.types.tags


class CreateBackupVaultInput(TypedDict, closed=True):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of letters, numbers, and hyphens.</p>"""
    backup_vault_tags: NotRequired["aws_sdk_backup.types.tags.Tags"]
    """<p>The tags to assign to the backup vault.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>The server-side encryption key that is used to protect your backups; for example, <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p>"""
    creator_request_id: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. This parameter is optional.</p> <p>If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackupVaultInput) -> dict:
    out: dict = {}
    if "backup_vault_tags" in value:
        import aws_sdk_backup.types.tags

        out["BackupVaultTags"] = aws_sdk_backup.types.tags.serialize_json(
            value["backup_vault_tags"]
        )
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    return out


def deserialize_json(data: dict) -> CreateBackupVaultInput:
    out: CreateBackupVaultInput = {}  # type: ignore[typeddict-item]
    if "BackupVaultTags" in data:
        import aws_sdk_backup.types.tags

        out["backup_vault_tags"] = aws_sdk_backup.types.tags.deserialize_json(
            data["BackupVaultTags"]
        )
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    return out
