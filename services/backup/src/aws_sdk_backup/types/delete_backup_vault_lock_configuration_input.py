"""Generated from Smithy shape ``com.amazonaws.backup#DeleteBackupVaultLockConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_vault_name


class DeleteBackupVaultLockConfigurationInput(TypedDict, closed=True):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of the backup vault from which to delete Backup Vault Lock.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBackupVaultLockConfigurationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBackupVaultLockConfigurationInput:
    out: DeleteBackupVaultLockConfigurationInput = {}  # type: ignore[typeddict-item]
    return out
