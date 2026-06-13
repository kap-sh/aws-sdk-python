"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupVaultNotificationsInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_vault_name


class GetBackupVaultNotificationsInput(TypedDict):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupVaultNotificationsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBackupVaultNotificationsInput:
    out: GetBackupVaultNotificationsInput = {}  # type: ignore[typeddict-item]
    return out
