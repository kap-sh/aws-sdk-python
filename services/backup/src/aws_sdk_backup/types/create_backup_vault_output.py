"""Generated from Smithy shape ``com.amazonaws.backup#CreateBackupVaultOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.timestamp


class CreateBackupVaultOutput(TypedDict):
    backup_vault_name: NotRequired[
        "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Region where they are created. They consist of lowercase letters, numbers, and hyphens.</p>"""
    backup_vault_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example, <code>arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault</code>.</p>"""
    creation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time a backup vault is created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationDate</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackupVaultOutput) -> dict:
    out: dict = {}
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "backup_vault_arn" in value:
        out["BackupVaultArn"] = value["backup_vault_arn"]
    if "creation_date" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationDate"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> CreateBackupVaultOutput:
    out: CreateBackupVaultOutput = {}  # type: ignore[typeddict-item]
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    if "BackupVaultArn" in data:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if "CreationDate" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    return out
