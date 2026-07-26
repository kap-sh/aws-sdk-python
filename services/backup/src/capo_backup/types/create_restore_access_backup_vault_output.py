"""Generated from Smithy shape ``com.amazonaws.backup#CreateRestoreAccessBackupVaultOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.arn
    import capo_backup.types.backup_vault_name
    import capo_backup.types.timestamp
    import capo_backup.types.vault_state


class CreateRestoreAccessBackupVaultOutput(TypedDict, closed=True):
    restore_access_backup_vault_arn: NotRequired["capo_backup.types.arn.ARN"]
    """<p>The ARN that uniquely identifies the created restore access backup vault.</p>"""
    vault_state: NotRequired["capo_backup.types.vault_state.VaultState"]
    """<p>The current state of the restore access backup vault.</p>"""
    restore_access_backup_vault_name: NotRequired[
        "capo_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>The name of the created restore access backup vault.</p>"""
    creation_date: NotRequired["capo_backup.types.timestamp.timestamp"]
    """<p>>The date and time when the restore access backup vault was created, in Unix format and Coordinated Universal Time </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRestoreAccessBackupVaultOutput) -> dict:
    out: dict = {}
    if "restore_access_backup_vault_arn" in value:
        out["RestoreAccessBackupVaultArn"] = value["restore_access_backup_vault_arn"]
    if "vault_state" in value:
        import capo_backup.types.vault_state

        out["VaultState"] = capo_backup.types.vault_state.serialize_json(
            value["vault_state"]
        )
    if "restore_access_backup_vault_name" in value:
        out["RestoreAccessBackupVaultName"] = value["restore_access_backup_vault_name"]
    if "creation_date" in value:
        import capo_backup.types.timestamp

        out["CreationDate"] = capo_backup.types.timestamp.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> CreateRestoreAccessBackupVaultOutput:
    out: CreateRestoreAccessBackupVaultOutput = {}  # type: ignore[typeddict-item]
    if "RestoreAccessBackupVaultArn" in data:
        out["restore_access_backup_vault_arn"] = data["RestoreAccessBackupVaultArn"]
    if "VaultState" in data:
        import capo_backup.types.vault_state

        out["vault_state"] = capo_backup.types.vault_state.deserialize_json(
            data["VaultState"]
        )
    if "RestoreAccessBackupVaultName" in data:
        out["restore_access_backup_vault_name"] = data["RestoreAccessBackupVaultName"]
    if "CreationDate" in data:
        import capo_backup.types.timestamp

        out["creation_date"] = capo_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    return out
