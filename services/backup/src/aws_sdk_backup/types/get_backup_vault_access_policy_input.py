"""Generated from Smithy shape ``com.amazonaws.backup#GetBackupVaultAccessPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_vault_name


class GetBackupVaultAccessPolicyInput(TypedDict, closed=True):
    backup_vault_name: "aws_sdk_backup.types.backup_vault_name.BackupVaultName"
    """<p>The name of a logical container where backups are stored. Backup vaults are identified by names that are unique to the account used to create them and the Amazon Web Services Region where they are created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBackupVaultAccessPolicyInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBackupVaultAccessPolicyInput:
    out: GetBackupVaultAccessPolicyInput = {}  # type: ignore[typeddict-item]
    return out
