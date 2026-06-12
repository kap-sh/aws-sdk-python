"""Generated from Smithy shape ``com.amazonaws.backup#CreateRestoreAccessBackupVaultOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.timestamp
    import aws_sdk_backup.types.vault_state

class CreateRestoreAccessBackupVaultOutput(TypedDict):
    restore_access_backup_vault_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>The ARN that uniquely identifies the created restore access backup vault.</p>"""
    vault_state: NotRequired["aws_sdk_backup.types.vault_state.VaultState"]
    """<p>The current state of the restore access backup vault.</p>"""
    restore_access_backup_vault_name: NotRequired["aws_sdk_backup.types.backup_vault_name.BackupVaultName"]
    """<p>The name of the created restore access backup vault.</p>"""
    creation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>>The date and time when the restore access backup vault was created, in Unix format and Coordinated Universal Time </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateRestoreAccessBackupVaultOutput) -> dict:
    out: dict = {}
    if "restore_access_backup_vault_arn" in value:
        out["RestoreAccessBackupVaultArn"] = value["restore_access_backup_vault_arn"]
    if "vault_state" in value:
        import aws_sdk_backup.types.vault_state
        out["VaultState"] = aws_sdk_backup.types.vault_state.serialize_json(value["vault_state"])
    if "restore_access_backup_vault_name" in value:
        out["RestoreAccessBackupVaultName"] = value["restore_access_backup_vault_name"]
    if "creation_date" in value:
        import aws_sdk_backup.types.timestamp
        out["CreationDate"] = aws_sdk_backup.types.timestamp.serialize_json(value["creation_date"])
    return out


def deserialize_json(data: dict) -> CreateRestoreAccessBackupVaultOutput:
    out: CreateRestoreAccessBackupVaultOutput = {}  # type: ignore[typeddict-item]
    if "RestoreAccessBackupVaultArn" in data:
        out["restore_access_backup_vault_arn"] = data["RestoreAccessBackupVaultArn"]
    if "VaultState" in data:
        import aws_sdk_backup.types.vault_state
        out["vault_state"] = aws_sdk_backup.types.vault_state.deserialize_json(data["VaultState"])
    if "RestoreAccessBackupVaultName" in data:
        out["restore_access_backup_vault_name"] = data["RestoreAccessBackupVaultName"]
    if "CreationDate" in data:
        import aws_sdk_backup.types.timestamp
        out["creation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(data["CreationDate"])
    return out