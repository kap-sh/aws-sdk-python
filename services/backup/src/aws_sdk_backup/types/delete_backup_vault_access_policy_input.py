"""Generated from Smithy shape ``com.amazonaws.backup#DeleteBackupVaultAccessPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_vault_name


class DeleteBackupVaultAccessPolicyInput(TypedDict, closed=True):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created. They consist of lowercase letters, numbers, and hyphens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBackupVaultAccessPolicyInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBackupVaultAccessPolicyInput:
    out: DeleteBackupVaultAccessPolicyInput = {}  # type: ignore[typeddict-item]
    return out
