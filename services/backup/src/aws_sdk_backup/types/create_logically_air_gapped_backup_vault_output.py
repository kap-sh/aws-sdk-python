"""Generated from Smithy shape ``com.amazonaws.backup#CreateLogicallyAirGappedBackupVaultOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_name
    import aws_sdk_backup.types.timestamp
    import aws_sdk_backup.types.vault_state


class CreateLogicallyAirGappedBackupVaultOutput(TypedDict, closed=True):
    backup_vault_name: NotRequired[
        "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    ]
    """<p>The name of a logical container where backups are stored. Logically air-gapped backup vaults are identified by names that are unique to the account used to create them and the Region where they are created.</p>"""
    backup_vault_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>The ARN (Amazon Resource Name) of the vault.</p>"""
    creation_date: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time when the vault was created.</p> <p>This value is in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    vault_state: NotRequired["aws_sdk_backup.types.vault_state.VaultState"]
    """<p>The current state of the vault.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateLogicallyAirGappedBackupVaultOutput) -> dict:
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
    if "vault_state" in value:
        import aws_sdk_backup.types.vault_state

        out["VaultState"] = aws_sdk_backup.types.vault_state.serialize_json(
            value["vault_state"]
        )
    return out


def deserialize_json(data: dict) -> CreateLogicallyAirGappedBackupVaultOutput:
    out: CreateLogicallyAirGappedBackupVaultOutput = {}  # type: ignore[typeddict-item]
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    if "BackupVaultArn" in data:
        out["backup_vault_arn"] = data["BackupVaultArn"]
    if "CreationDate" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_date"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationDate"]
        )
    if "VaultState" in data:
        import aws_sdk_backup.types.vault_state

        out["vault_state"] = aws_sdk_backup.types.vault_state.deserialize_json(
            data["VaultState"]
        )
    return out
